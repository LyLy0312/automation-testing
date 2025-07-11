from playwright.sync_api import Page, expect


class ElectronicsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.location_button = page.locator("button:has-text('Vị trí')")
        self.modal = page.locator("label:has-text('Tp Hồ Chí Minh')").first.locator("..").locator("..")
        self.city_option = lambda name: self.modal.locator(f"label:has-text('{name}')")
        self.confirm_btn = self.modal.locator("button:has-text('Xác nhận')")

    def open_location_picker(self) -> None:
        self.location_button.click()
        expect(self.city_option("Tp Hồ Chí Minh")).to_be_visible(timeout=10000)

    def choose_city(self, city: str) -> None:
        option = self.city_option(city)
        option.scroll_into_view_if_needed()
        expect(option).to_be_visible(timeout=5000)
        option.click()

    def confirm(self, city: str) -> None:
        self.page.locator("button:has-text('Xác nhận')").click()
        actual_text = self.location_button.inner_text(timeout=5000)
        city_text = actual_text.split("\n")[-1].strip()
        assert city_text.lower() == city.lower(), f"Expected '{city}', but got '{city_text}'"

    def selected_city(self) -> str:
        full_text = self.location_button.inner_text()
        return full_text.split("\n")[-1].strip()

    def location_is(self, expected: str) -> bool:
        expect(self.location_button).to_have_text(expected, ignore_case=True)
        return True
