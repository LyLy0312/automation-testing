from playwright.sync_api import Page

class GitHubProfilePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_profile(self):
        self.page.goto("https://github.com/")
        avatar_button = self.page.locator("button[aria-label='Open user navigation menu']")
        avatar_button.wait_for(state="visible")
        avatar_button.click()

        # Click vào 'Your profile' dựa vào href của thẻ <a>
        profile_link = self.page.locator("a[href='/lili23-wq']")
        profile_link.wait_for(state="visible")
        profile_link.click()

    def take_screenshot_of_tab(self, tab_name: str, filename: str):
        tab_ids = {
            "Overview": "overview-tab",
            "Repositories": "repositories-tab",
            "Projects": "projects-tab",
            "Packages": "packages-tab",
            "Stars": "stars-tab",
        }
        tab_id = tab_ids.get(tab_name)
        if not tab_id:
            raise ValueError(f"Unknown tab: {tab_name}")
        tab_locator = self.page.locator(f"a#{tab_id}")
        tab_locator.wait_for(state="visible")
        tab_locator.click()

        self.page.wait_for_timeout(1000)
        self.page.screenshot(path=filename, full_page=True)
        print(f"Screenshot saved: {filename}")
        import os
        print("Đang chạy ở thư mục:", os.getcwd())



