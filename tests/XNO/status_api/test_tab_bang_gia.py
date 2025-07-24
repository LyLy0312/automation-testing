import pytest
import allure
from xno_base_test import XNOBaseTest

class TestTabBangGia:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/bang-gia", "Bảng giá")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Bảng giá")
    def test_bang_gia_click_subtabs(self):
        self.tracker.set_section("Bảng giá")
        self.page.locator("a:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Ngành hiển thị Dropdown")
        self.page.locator("button:has-text('Tất cả các ngành')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Bỏ tick VN30 và Thép")
        self.page.locator("label:has-text('VN30')").click()
        self.page.locator("label:has-text('Thép')").click()

        self.tracker.set_section("Click ngoài để đóng Dropdown")
        self.page.mouse.click(0, 0)
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Modal Thêm mã CK")
        self.page.locator("button:has-text('Thêm mã CK')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Nhập mã TCB")
        self.page.locator("input[type='text']").fill("TCB")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn mã TCB")
        self.page.locator("span:has-text('TCB')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Sau khi thêm mã TCB")
        self.page.locator("footer button:has-text('Thêm mã')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Modal HDG Tổng quan")
        self.page.locator("div[tabindex='0']:has-text('HDB')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Modal EVF Nhận định")
        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Nhận định")
        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab XChart AI")
        self.page.locator("button:has-text('XChart AI')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Biểu đồ RRG")
        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tab Dòng tiền thông minh")
        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Tài chính")
        self.page.locator("button:has-text('Tài chính')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Chỉ số tài chính")
        self.page.locator("button:has-text('Chỉ số tài chính')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Chỉ số tài chính Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Báo cáo tài chính")
        self.page.locator("button:has-text('Báo cáo tài chính')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Báo cáo tài chính Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(1000)

        self.tracker.set_section("Tab Kết quả kinh doanh")
        self.page.locator("button:has-text('Kết quả kinh doanh')").click()

        self.tracker.set_section("Kết quả kinh doanh Hàng quý")
        self.page.locator("button:has-text('Hàng quý')").click()

        self.tracker.set_section("Tab Lưu chuyển tiền tệ")
        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()

        self.tracker.set_section("Lưu chuyển tiền tệ Hàng năm")
        self.page.locator("button:has-text('Hàng năm')").click()

        self.tracker.set_section("Tab Hồ sơ công ty")
        self.page.locator("button:has-text('Hồ sơ')").click()

        self.tracker.set_section("Tab Cổ đông & GD nội bộ")
        self.page.locator("button:has-text('Cổ đông & GD nội bộ')").click()

        self.tracker.set_section("Đóng Modal")
        self.page.locator("button[aria-label='Close']").click()

        self.tracker.print_summary()