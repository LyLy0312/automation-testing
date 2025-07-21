"""
This module contains shared fixtures.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

# from pages.Duckduckgo.result import DuckDuckGoResultPage
# from pages.Duckduckgo.search import DuckDuckGoSearchPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
# DuckDuckGo search fixtures
# ------------------------------------------------------------

# @pytest.fixture
# def result_page(page: Page) -> DuckDuckGoResultPage:
#     return DuckDuckGoResultPage(page)
#
#
# @pytest.fixture
# def search_page(page: Page) -> DuckDuckGoSearchPage:
#     return DuckDuckGoSearchPage(page)


# ------------------------------------------------------------
# GitHub project fixtures
# ------------------------------------------------------------

# Environment variables

def _get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value


@pytest.fixture(scope='session')
def gh_username() -> str:
    return _get_env_var('GITHUB_USERNAME')


@pytest.fixture(scope='session')
def gh_password() -> str:
    return _get_env_var('GITHUB_PASSWORD')


@pytest.fixture(scope='session')
def gh_access_token() -> str:
    return _get_env_var('GITHUB_ACCESS_TOKEN')


@pytest.fixture(scope='session')
def gh_project_name() -> str:
    return _get_env_var('GITHUB_PROJECT_NAME')


# Request context

@pytest.fixture(scope='session')
def gh_context(
    playwright: Playwright,
    gh_access_token: str) -> Generator[APIRequestContext, None, None]:

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {gh_access_token}"}

    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers)

    yield request_context
    request_context.dispose()


# GitHub project requests

@pytest.fixture(scope='session')
def gh_project(
    gh_context: APIRequestContext,
    gh_username: str,
    gh_project_name: str) -> dict:

    resource = f'/users/{gh_username}/projects'
    response = gh_context.get(resource)
    expect(response).to_be_ok()

    name_match = lambda x: x['name'] == gh_project_name
    filtered = filter(name_match, response.json())
    project = list(filtered)[0]
    assert project

    return project


@pytest.fixture()
def project_columns(
    gh_context: APIRequestContext,
    gh_project: dict) -> list[dict]:

    response = gh_context.get(gh_project['columns_url'])
    expect(response).to_be_ok()

    columns = response.json()
    assert len(columns) >= 2
    return columns


@pytest.fixture()
def project_column_ids(project_columns: list[dict]) -> list[str]:
    return list(map(lambda x: x['id'], project_columns))

# from pages.Cho_tot.chotot_home import ChototHomePage
# from pages.Cho_tot.chotot_electronics import ElectronicsPage
# @pytest.fixture
# def home_page(page: Page) -> ChototHomePage:
#     return ChototHomePage(page)


# @pytest.fixture
# def electronics_page(page: Page) -> ElectronicsPage:
#     return ElectronicsPage(page)


#XNO (xóa naày mới chạy được Cho_tot,Duckduckgo,GitHub)

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=1000)
        yield browser
        browser.close()
#############################################
import pytest
from playwright.sync_api import sync_playwright
from utils.config import EMAIL, PASSWORD

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def login(page):
    page.goto("https://xno.vn/dang-nhap")
    page.locator("input[placeholder='Vui lòng nhập email...']").fill(EMAIL)
    page.locator("input[placeholder='Mật khẩu đăng nhập...']").fill(PASSWORD)
    page.locator("button[type='submit']:has-text('Đăng nhập')").click()

    page.wait_for_timeout(5000)
    print("URL sau khi login:", page.url)
    yield page


