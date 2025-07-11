# tests/test_github_login_and_screenshot.py

import pytest
from pages.Github.profile import GitHubProfilePage

TABS = [
    ("Overview", "overview.png"),
    ("Repositories", "repositories.png"),
    ("Projects", "projects.png"),
    ("Packages", "packages.png"),
    ("Stars", "stars.png")
]

@pytest.fixture(scope="function")
def context_with_login(browser):
    # Tạo context mới với state đã lưu
    context = browser.new_context(storage_state="../state.json")
    yield context
    context.close()

def test_github_profile_screenshots(context_with_login):
    page = context_with_login.new_page()
    profile_page = GitHubProfilePage(page)

    # Mở trang profile
    profile_page.go_to_profile()

    # Lặp qua từng tab và chụp hình
    for tab_name, filename in TABS:
        import os

        output_path = os.path.join("..", "screenshots", filename)
        profile_page.take_screenshot_of_tab(tab_name, output_path)

