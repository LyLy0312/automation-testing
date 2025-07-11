from playwright.sync_api import Page

class HomePage:
    URL = "https://www.chotot.com"

    def __init__(self, page: Page):
        self.page = page
        self.real_estate_category = page.locator("img[alt='Bất động sản']")

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
        except:
            pass

    def close_signup_banner_if_exists(self):
        try:
            close_button = self.page.locator("div[role='dialog'] button >> text='×'")
            if close_button.is_visible():
                close_button.click()
                self.page.wait_for_timeout(500)
        except:
            pass

    def dismiss_overlay_by_clicking(self):
        try:
            if self.page.locator("div.aw__s1tlv3pf").is_visible():
                self.page.mouse.click(10, 10)
                self.page.wait_for_timeout(500)
        except:
            pass

    def go_to_real_estate(self):
        self.real_estate_category.click()