from playwright.sync_api import Page


class ChototHomePage:

    URL = "https://www.chotot.com"

    def __init__(self, page: Page):
        self.page = page
        self.electronics_category = page.locator("img[alt='Đồ điện tử']")

    def load(self):
        self.page.goto(self.URL)
        self.close_region_modal_if_exists()

    def close_region_modal_if_exists(self):
        try:
            close_button = self.page.locator("button.aw__caiukm8")
            if close_button.is_visible():
                close_button.click()

                overlay = self.page.locator("div.aw__s1tlv3pf")
                overlay.wait_for(state="hidden", timeout=10000)
        except Exception as e:
            print("Không thể đóng modal:", e)

    def close_signup_banner_if_exists(self):
            close_button = self.page.locator("div[role='dialog'] button >> text='×'")
            if close_button.is_visible():
                close_button.click()
                self.page.wait_for_timeout(500)

    def dismiss_overlay_by_clicking(self):
        try:
            if self.page.locator("div.aw__s1tlv3pf").is_visible():
                self.page.mouse.click(10, 10)
                self.page.wait_for_timeout(500)
        except:
            pass
    def go_to_electronics(self):
        self.electronics_category.click()

