import pytest
import allure
from xno_base_test import XNOBaseTest

class TestTabGiaoDich:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/giao-dich", "Giao dịch")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Giao dịch")
    def test_giao_dich_click_subtabs(self):
        frame = self.page.frame_locator("iframe[src*='vi-tv-chart']")

        self.tracker.set_section("Giao dịch - Biểu đồ mặc định")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Timeframe Dropdown")
        frame.locator("#header-toolbar-intervals div[data-role='button'] .value-2y-wa9jT", has_text="D").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn Timeframe 1W")
        frame.locator("div[data-value='1W']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Dropdown Kiểu biểu đồ")
        frame.locator("#header-toolbar-chart-styles div[data-role='button'][title*='Biểu đồ']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn kiểu biểu đồ hình thanh")
        frame.locator("div[data-value='bar']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Dropdown Chỉ báo")
        frame.locator("#header-toolbar-indicators div[data-role='button']:has-text('Các chỉ báo')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn chỉ báo Aroon")
        frame.locator("span:has-text('Aroon')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn chỉ báo Biến động Chaikin")
        frame.locator("span:has-text('Biến động Chaikin')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tìm kiếm chỉ báo TRIX")
        frame.locator("input[placeholder*='Tìm kiếm']").fill("TRIX")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn chỉ báo TRIX")
        frame.locator("span:has-text('TRIX')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Đóng popup chỉ báo")
        frame.locator("span[data-role='button'][data-name='close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Khôi phục chỉ báo")
        frame.locator("div[data-role='button'].buttonUndo-nGqa616C").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hiển lại chỉ báo")
        redo_button = frame.locator("div[data-role='button'].buttonUndo-nGqa616C").nth(1)
        if redo_button.is_visible() and "isDisabled" not in (redo_button.get_attribute("class") or ""):
            redo_button.click()
        else:
            print("Redo button is either hidden or disabled.")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Mở modal cài đặt")
        frame.locator("#header-toolbar-properties").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Mã")
        frame.locator("span.titleText-DggvOZTm:has-text('Mã')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Checkbox Mã")
        frame.locator("label:has-text('Các Thanh màu Dựa trên giá Đóng cửa Phiên trước')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Dòng trạng thái")
        frame.locator("span.titleText-DggvOZTm:has-text('Dòng trạng thái')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Dropdown Mô tả")
        frame.locator("div[data-section-name='symbolTextSource'] [data-role='listbox']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn mô tả Ticker")
        frame.locator("div[role='option']:has-text('Ticker')").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Các tỷ lệ")
        frame.locator("span.titleText-DggvOZTm:has-text('Các tỷ lệ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Biểu tượng Nhãn tên Checked")
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Biểu tượng Nhãn tên Unchecked")
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Diện mạo")
        frame.locator("span.titleText-DggvOZTm:has-text('Diện mạo')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn hình nền Dropdown")
        frame.locator("span[data-role='listbox'][data-name='background-type-options-dropdown']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn Gradient")
        frame.locator("div[role='option']:has-text('Gradient')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Xác nhận modal cài đặt")
        frame.locator("button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Icon chụp ảnh")
        frame.locator("#header-toolbar-screenshot").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Lưu hình ảnh biểu đồ")
        frame.locator("div[data-name='save-chart-image']:has-text('Lưu hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Sao chép hình ảnh biểu đồ")
        frame.locator("#header-toolbar-screenshot").click()
        frame.locator("div[data-name='copy-chart-image']:has-text('Sao chép hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Thanh ngang VNINDEX")
        frame.locator("div[data-name='legend-source-title']:has-text('VNINDEX')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Ẩn layer VNINDEX")
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hiện layer VNINDEX")
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - 3 chấm layer VNINDEX")
        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Thứ tự trực quan")
        frame.locator("span:has-text('Thứ tự trực quan')").first.hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Chuyển tới")
        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Ghim theo Tỷ lệ")
        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Bên phải)')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Đường")
        frame.locator("span:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Thông tin Mã giao dịch")
        frame.locator("span:has-text('Thông tin Mã giao dịch…')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Đóng thông tin Mã giao dịch")
        frame.locator("div.header-2ibjJG9Z span.close-2ibjJG9Z").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Ẩn layer Khối lượng")
        frame.locator("div.titleWrapper-2KhwsEwE:has-text('Khối lượng')").click()
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hiện layer Khối lượng")
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Setting Khối lượng")
        frame.locator("[data-name='legend-settings-action']").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Checkbox Đóng cửa trước")
        frame.locator("label:has-text('Dựa trên màu của phiên đóng cửa trước')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Định dạng")
        frame.locator("[data-name='tab-item-style']:has-text('Định dạng')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tick Volume MA")
        frame.locator("label:has-text('Volume MA')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tab Hiển thị")
        frame.locator("[data-name='tab-item-visibilities']:has-text('Hiển thị')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Tick Tuần")
        frame.locator("label:has-text('Tuần')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Các mặc định")
        frame.locator("span#study-defaults-manager:has-text('Các mặc định')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Xác nhận OK Khối lượng")
        frame.locator("span.submitButton-KW8170fm button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - 3 chấm layer Khối lượng")
        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Thứ tự trực quan Volume")
        frame.locator("span:has-text('Thứ tự Trực quan')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Chuyển tới Volume")
        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Ghim Volume")
        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Không có Tỷ lệ)')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Sao chép Volume")
        frame.locator("span:has-text('Sao chép')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Open Setting")
        frame.locator("div.wrapper-1DJMiIgd").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Nhãn")
        frame.locator("span.label-f5BaKrKq:has-text('Nhãn')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Hover Đường")
        frame.locator("span.label-f5BaKrKq:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Reset Scale")
        frame.locator("span.label-f5BaKrKq:has-text('Đặt lại thang giá')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Timeframe 2W")
        frame.locator("div.item-3SbREAgE:has-text('2w')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Open Time Axis Setting")
        frame.locator("[data-name='go-to-date']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn ngày 13-07-2025")
        frame.locator("span[data-day='2025-07-13']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Phạm vi tùy chỉnh")
        frame.locator("[data-name='tab-item-customrange']:has-text('Phạm vi tùy chỉnh')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn từ ngày 11-07-2025")
        frame.locator("span[data-day='2025-07-11']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn đến ngày 17-07-2025")
        frame.locator("span[data-day='2025-07-17']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Xác nhận Phạm vi tùy chỉnh")
        frame.locator("span.submitButton-KW8170fm:has-text('Đến')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn múi giờ Dropdown")
        frame.locator("[data-name='time-zone-menu']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Chọn múi giờ UTC-6 Denver")
        frame.locator("span:has-text('(UTC-6) Denver')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Click Log")
        frame.locator("div.text-2Vpz_LXc:has-text('log')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Giao dịch - Click Tự động")
        frame.locator("div.text-2Vpz_LXc:has-text('tự động')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()