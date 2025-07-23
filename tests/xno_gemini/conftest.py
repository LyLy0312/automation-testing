import base64
import logging
import os
import platform
import sys
from importlib.metadata import version
from typing import AsyncGenerator, Dict, Optional
from enum import Enum
import unicodedata

import allure
import pytest
from browser_use import Agent, BrowserProfile, BrowserSession
from browser_use.llm import ChatGoogle
from browser_use.utils import get_browser_use_version
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path=env_path)
print("DEBUG EMAIL =", os.getenv("EMAIL"))
print("DEBUG PASSWORD =", os.getenv("PASSWORD"))

class BrowserChannel(Enum):
    CHROME = "chrome"
    MSEDGE = "msedge"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


@pytest.fixture(scope="session")
def browser_version_info(browser_profile: BrowserProfile) -> Dict[str, str]:
    try:
        playwright_version = version("playwright")
        with sync_playwright() as p:
            browser_type = p.chromium
            launch_args = {}

            if browser_profile.channel:
                launch_args["channel"] = browser_profile.channel.value

            browser = browser_type.launch(**launch_args)
            browser_version = browser.version
            browser.close()

        return {
            "playwright_version": playwright_version,
            "browser_version": browser_version,
        }
    except Exception as e:
        logging.warning(f"Could not determine Playwright/browser version: {e}")
        return {
            "playwright_version": "N/A",
            "browser_version": "N/A",
        }


@pytest.fixture(scope="session", autouse=True)
def environment_reporter(
    request: pytest.FixtureRequest,
    llm: ChatGoogle,
    browser_profile: BrowserProfile,
    browser_version_info: Dict[str, str],
):
    allure_dir = request.config.getoption("--alluredir")
    if not allure_dir or not isinstance(allure_dir, str):
        return

    ENVIRONMENT_PROPERTIES_FILENAME = "environment.properties"
    properties_file = os.path.join(allure_dir, ENVIRONMENT_PROPERTIES_FILENAME)

    try:
        os.makedirs(allure_dir, exist_ok=True)
    except PermissionError:
        logging.error(f"Permission denied to create report directory: {allure_dir}")
        return

    env_props = {
        "operating_system": f"{platform.system()} {platform.release()}",
        "python_version": sys.version.split(" ")[0],
        "browser_use_version": get_browser_use_version(),
        "playwright_version": browser_version_info["playwright_version"],
        "browser_type": (
            browser_profile.channel.value if browser_profile.channel else "chromium"
        ),
        "browser_version": browser_version_info["browser_version"],
        "headless_mode": str(browser_profile.headless),
        "llm_model": llm.model,
    }

    try:
        with open(properties_file, "w") as f:
            for key, value in env_props.items():
                f.write(f"{key}={value}\n")
    except IOError as e:
        logging.error(f"Failed to write environment properties file: {e}")


@pytest.fixture(scope="session")
def llm() -> ChatGoogle:
    DEFAULT_MODEL = "gemini-2.0-flash"
    model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
    return ChatGoogle(model=model_name)


@pytest.fixture(scope="session")
def browser_profile() -> BrowserProfile:
    headless_mode = os.getenv("HEADLESS", "True").lower() in ("true", "1", "t")
    return BrowserProfile(
        headless=headless_mode,
        channel=BrowserChannel.MSEDGE
    )


@pytest.fixture(scope="function")
async def browser_session(
    browser_profile: BrowserProfile,
) -> AsyncGenerator[BrowserSession, None]:
    session = BrowserSession(browser_profile=browser_profile)
    yield session
    await session.close()


# --- Base Test Class for Agent-based Tests ---

class BaseAgentTest:

    BASE_URL = "https://xno.vn/giao-dich"

    def normalize_string(self, s: str) -> str:
        # Chuyển đổi ký tự có dấu thành không dấu
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn').lower()

    async def validate_task(
        self,
        llm: ChatGoogle,
        browser_session: BrowserSession,
        task_instruction: str,
        expected_substring: Optional[str] = None,
        ignore_case: bool = False,
    ) -> str:
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        task_instruction = task_instruction.format(email=email, password=password)

        full_task = task_instruction  # Không thêm BASE_URL vì đã được đưa vào task

        result_text = await run_agent_task(full_task, llm, browser_session)

        assert result_text is not None, "Agent did not return a final result."

        if expected_substring:
            result_to_check = self.normalize_string(result_text) if ignore_case else result_text
            substring_to_check = self.normalize_string(expected_substring) if ignore_case else expected_substring
            assert (
                substring_to_check in result_to_check
            ), f"Assertion failed: Expected '{expected_substring}' not found in agent result: '{result_text}'"

        return result_text


# --- Allure Step Reporting ---

async def record_step(agent: Agent):
    history = agent.state.history
    if not history:
        return

    last_action = history.model_actions()[-1] if history.model_actions() else {}
    action_name = next(iter(last_action)) if last_action else "No action"
    action_params = last_action.get(action_name, {})

    step_title = f"Action: {action_name}"
    if action_params:
        param_str = ", ".join(f"{k}={v}" for k, v in action_params.items())
        step_title += f"({param_str})"

    with allure.step(step_title):
        thoughts = history.model_thoughts()
        if thoughts:
            allure.attach(
                str(thoughts[-1]),
                name="Agent Thoughts",
                attachment_type=allure.attachment_type.TEXT,
            )

        url = history.urls()[-1] if history.urls() else "N/A"
        allure.attach(
            url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )

        last_history_item = history.history[-1] if history.history else None
        if last_history_item and last_history_item.metadata:
            duration = last_history_item.metadata.duration_seconds
            allure.attach(
                f"{duration:.2f}s",
                name="Step Duration",
                attachment_type=allure.attachment_type.TEXT,
            )

        if agent.browser_session:
            try:
                screenshot_b64 = await agent.browser_session.take_screenshot()
                if screenshot_b64:
                    screenshot_bytes = base64.b64decode(screenshot_b64)
                    allure.attach(
                        screenshot_bytes,
                        name="Screenshot after Action",
                        attachment_type=allure.attachment_type.PNG,
                    )
            except Exception as e:
                logging.warning(f"Failed to take or attach screenshot: {e}")


# --- Agent runner ---

@allure.step("Running browser agent with task: {task_description}")
async def run_agent_task(
    task_description: str,
    llm: ChatGoogle,
    browser_session: BrowserSession,
) -> Optional[str]:
    logging.info(f"Running task: {task_description}")

    agent = Agent(
        task=task_description,
        llm=llm,
        browser_session=browser_session,
        name=f"Agent for '{task_description[:50]}...'",
    )

    result = await agent.run(on_step_end=record_step)

    final_text = result.final_result()
    allure.attach(
        final_text,
        name="Agent Final Output",
        attachment_type=allure.attachment_type.TEXT,
    )

    logging.info("Task finished.")
    return final_text