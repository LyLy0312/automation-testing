import pytest
import allure
from xno_base_test import XNOBaseTest

class TestBaoCaoPhanTich:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/giao-dich", "Báo cáo phân tích")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Chọn Báo cáo phân tích và thao tác dropdown")
    def test_baocao_phantich_and_dropdown(self):
        self.tracker.set_section("Truy cập Báo cáo phân tích")
        self.page.locator("button[data-key='baocaophantich']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Mở dropdown Loại báo cáo")
        self.page.locator("button[aria-haspopup='listbox']:has(span:text('Loại báo cáo'))").click()
        self.page.wait_for_timeout(1000)

        options = ["Tất cả", "Báo cáo Thị Trường", "Báo cáo Ngành", "Báo cáo Vĩ mô", "Cổ phiếu", "Khác"]
        for i, option in enumerate(options, 1):
            self.tracker.set_section(f"Chọn {option}")
            self.page.locator(f"li[role='option']:has(span:text('{option}'))").click()
            self.page.wait_for_timeout(2000)
            if i < len(options):
                dropdown = self.page.locator(f"button[aria-haspopup='listbox']:has(span:text('{option}'))")
                dropdown.click()
                self.page.wait_for_timeout(1000)

        self.tracker.set_section("Nhấp nút Xem đầu tiên")
        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Đóng modal")
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Nhấp nút Xem thứ hai")
        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Đóng modal lần nữa")
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)

        self.tracker.print_summary()