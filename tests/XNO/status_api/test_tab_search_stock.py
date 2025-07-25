import pytest
import allure
from xno_base_test import XNOBaseTest

class TestSearchStockCode:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/bang-gia", "search stock")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Tìm kiếm mã chứng khoán")
    def test_search_stock_pet(self):
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tìm kiếm mã PET")
        self.page.locator("button[aria-haspopup='dialog']").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Nhập mã PET vào ô tìm kiếm")
        self.page.locator("input[aria-label='Tìm mã CK']").fill("PET")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn kết quả tìm kiếm PET")
        self.page.locator("div.font-bold:has-text('PET')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 1")
        self.page.locator("div.group:has(div:has-text('CCI Trend Confirmation'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 2")
        self.page.locator("div.group:has(div:has-text('Rolling Correlation Divergence'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 3")
        self.page.locator("div.group:has(div:has-text('Volume ROC Confirmation'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 4")
        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Reversal'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 5")
        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Crossover'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn bộ lọc của XBot TA - 6")
        self.page.locator("div.group:has(div:has-text('ROC Breakout'))").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Modal EVF Nhận định")
        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Nhận định")
        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab XChart AI")
        self.page.locator("button:has-text('XChart AI')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Biểu đồ RRG")
        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Dòng tiền thông minh")
        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Tài chính")
        self.page.locator("button:has-text('Tài chính')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Chỉ số tài chính")
        self.page.locator("button:has-text('Chỉ số tài chính')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chỉ số tài chính Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Báo cáo tài chính")
        self.page.locator("button:has-text('Báo cáo tài chính')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Báo cáo tài chính Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Kết quả kinh doanh")
        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Kết quả kinh doanh Hàng quý")
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Lưu chuyển tiền tệ")
        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lưu chuyển tiền tệ Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Hồ sơ công ty")
        self.page.locator("button:has-text('Hồ sơ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Cổ đông & GD nội bộ")
        self.page.locator("button:has-text('Cổ đông & GD nội bộ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Đóng Modal")
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()