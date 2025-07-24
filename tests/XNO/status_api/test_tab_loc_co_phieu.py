import pytest
import allure
from xno_base_test import XNOBaseTest

class TestTabLocCoPhieu:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/loc-co-phieu", "Lọc cổ phiếu")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Lọc cổ phiếu")
    def test_loc_co_phieu_click_subtabs(self):
        self.tracker.set_section("Lọc cổ phiếu - Cổ phiếu tăng trưởng lần 1")
        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu tăng trưởng')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Cổ phiếu tăng trưởng lần 2")
        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu giá trị')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Nhóm biến động giá")
        self.page.locator("div.relative.flex.h-8.w-full.cursor-pointer:has-text('Nhóm biến động giá')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Nhóm thông dụng")
        self.page.locator("div.relative.flex.h-8.w-full.cursor-pointer:has-text('Nhóm thông dụng')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Giá trị giao dịch trung bình 50 phiên")
        self.page.locator("div:has-text('Giá trị giao dịch trung bình 50 phiên (tỷ)')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Giá trị giao dịch")
        self.page.locator("div:has-text('Giá trị giao dịch (tỷ)')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Chọn mã BID")
        self.page.locator("div.font-semibold:has-text('BID')").first.click()
        self.page.wait_for_url("https://xno.vn/loc-co-phieu?symbol=BID&chiTietMaCK=true", timeout=20000)
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Bảng giá")
        self.page.locator("button[data-key='banggia']:has-text('Bảng giá')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Nhận định")
        self.page.locator("button[data-key='nhandinh']:has-text('Nhận định')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Tài chính")
        self.page.locator("button[data-key='phantichtaichinh']:has-text('Tài chính')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Chỉ số tài chính")
        self.page.locator("button[data-key='chisotaichinh']:has-text('Chỉ số tài chính')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Báo cáo tài chính")
        self.page.locator("button[data-key='baocaotaichinh']:has-text('Báo cáo tài chính')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Hồ sơ")
        self.page.locator("button[data-key='thongtindoanhnghiep']:has-text('Hồ sơ')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Tab Cổ đông & GD nội bộ")
        self.page.locator("button[data-key='codong']:has-text('Cổ đông & GD nội bộ')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Lọc cổ phiếu - Đóng Modal")
        self.page.locator("button[aria-label='Close']").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()