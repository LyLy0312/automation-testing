import os
import allure
from playwright.sync_api import Page
from utils.decorators import screenshot_decorator

class XNODashboardPageDirect:
    def __init__(self, page: Page):
        self.page = page

    @screenshot_decorator
    def screenshot(self, name: str):
        # Trigger screenshot with decorator
        pass

    # Capture detailed interactions in "Giao dịch" tab
    @allure.feature("Giao dịch")
    def capture_tab_giao_dich_and_subtabs(self):
        self.page.wait_for_timeout(2000)
        self.screenshot("0_1_giao_dich_bieu_do_mac_dinh.png")

        # Access the chart iframe
        frame = self.page.frame_locator("iframe[src*='vi-tv-chart']")

        # Click on the "1D" timeframe dropdown
        frame.locator("#header-toolbar-intervals div[data-role='button'] .value-2y-wa9jT", has_text="D").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_1_giao_dich__dropdown_timeframe.png")

        # Click on the "1W" timeframe option
        frame.locator("div[data-value='1W']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_2_giao_dich__chon_timeframe_1w.png")

        # Click on the chart styles dropdown
        frame.locator("#header-toolbar-chart-styles div[data-role='button'][title*='Biểu đồ']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_3_giao_dich__dropdown_kieu_bieu_do.png")

        # Click on the "Bar" chart style
        frame.locator("div[data-value='bar']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_4_giao_dich__chon_kieu_bieu_do_hinh_thanh.png")

        # Click on the indicators dropdown
        frame.locator("#header-toolbar-indicators div[data-role='button']:has-text('Các chỉ báo')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_giao_dich__dropdown_chi_bao.png")

        # Click for the Aroon indicator
        frame.locator("span:has-text('Aroon')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_1_Aroon.png")

        # Click for the Chaikin Oscillator indicator
        frame.locator("span:has-text('Biến động Chaikin')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_2_ Biến đôộng chaikin.png")

        # Search for the TRIX indicator
        frame.locator("input[placeholder*='Tìm kiếm']").fill("TRIX")
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_3_ Tìm kiếm.png")

        # Click on the TRIX indicator
        frame.locator("span:has-text('TRIX')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_6_giao_dich__chon_chi_bao_trix.png")

        # Click on the "Close" button to close the indicators panel
        frame.locator("span[data-role='button'][data-name='close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_7_giao_dich__sau_khi_chon_chi_bao.png")

        # Click on the "Undo" button to undo the last action
        frame.locator("div[data-role='button'].buttonUndo-nGqa616C").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_8_giao_dich__khoi_phuc_chi_bao.png")

        # Click on the "Redo" button to redo the last undone action
        redo_button = frame.locator("div[data-role='button'].buttonUndo-nGqa616C").nth(1)
        # Check if the redo button is visible and not disabled
        if redo_button.is_visible() and "isDisabled" not in (redo_button.get_attribute("class") or ""):
            redo_button.click()
        else:
            print("Redo button is either hidden or disabled.")
        self.page.wait_for_timeout(2000)
        self.screenshot("1_9_giao_dich__hien_lai_chi_bao.png")

        # Click on the settings icon in the header toolbar
        frame.locator("#header-toolbar-properties").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_10_giao_dich__mo_modal_cai_dat.png")

        # Click on the "Mã" tab
        frame.locator("span.titleText-DggvOZTm:has-text('Mã')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_11_Mã.png")

        frame.locator("label:has-text('Các Thanh màu Dựa trên giá Đóng cửa Phiên trước')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_11_1_giao_dich__cai_dat_tab_ma_tick_checkbox.png")

        # Click on the "Dòng trạng thái" tab
        frame.locator("span.titleText-DggvOZTm:has-text('Dòng trạng thái')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_12_giao_dich__cai_dat_tab_dong_trang_thai.png")

        # Click on the dropdown to change the symbol text source
        frame.locator("div[data-section-name='symbolTextSource'] [data-role='listbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_13_giao_dich__cai_dat_dropdown_mo_ta.png")

        # Click on the "Ticker" option in the dropdown
        frame.locator("div[role='option']:has-text('Ticker')").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_14_giao_dich__cai_dat_mo_ta_chon_ticker.png")

        # Click on the "Các tỷ lệ" tab
        frame.locator("span.titleText-DggvOZTm:has-text('Các tỷ lệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_Cac-ti-lệ.png")

        # Click on the checkbox to toggle it on
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_1_giao_dich__bieu_tuong_nhan_ten_checked.png")

        #Click on the checkbox to toggle it off
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_2_giao_dich__bieu_tuong_nhan_ten_unchecked.png")

        # Click on the "Diện mạo" tab
        frame.locator("span.titleText-DggvOZTm:has-text('Diện mạo')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_16_giao_dich__tab_dien_mao.png")

        # Click on the dropdown to change the background type
        frame.locator("span[data-role='listbox'][data-name='background-type-options-dropdown']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_17_giao_dich__chon_hinh_nen_dropdown.png")

        # Click on the "Gradient" option in the dropdown
        frame.locator("div[role='option']:has-text('Gradient')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_18_giao_dich__chon_gradient.png")

        # Click on the "OK" button to confirm the settings
        frame.locator("button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_19_giao_dich__sau_khi_xac_nhan_modal_cai_dat.png")

        # Click on the screenshot icon in the header toolbar
        frame.locator("#header-toolbar-screenshot").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_20_giao_dich__icon_chup_anh.png")

        # Click on the "Lưu hình ảnh biểu đồ" option
        frame.locator("div[data-name='save-chart-image']:has-text('Lưu hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_21_giao_dich__luu_hinh_anh_bieu_do.png")

        # Click on the "Sao chép hình ảnh biểu đồ" option
        frame.locator("#header-toolbar-screenshot").click()
        frame.locator("div[data-name='copy-chart-image']:has-text('Sao chép hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_22_giao_dich__sao_chep_hinh_anh_bieu_do.png")

        # Click on the legend item for VNINDEX
        frame.locator("div[data-name='legend-source-title']:has-text('VNINDEX')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_23_giao_dich__thanh_ngang_vnindex1w.png")

        # Click on the "Show/Hide" button for the VNINDEX layer
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_24_giao_dich__an_layer_vnindex1w.png")

        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_25_giao_dich__hien_layer_vnindex1w.png")

        # Click on the settings icon for the VNINDEX layer
        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_26_giao_dich__3_cham_layer_vnindex1w.png")

        # Hover over various options in the VNINDEX layer settings
        frame.locator("span:has-text('Thứ tự trực quan')").first.hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_27_giao_dich__hover_thu_tu_truc_quan.png")

        # Hover over the "Chuyển tới" option
        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_28_giao_dich__hover_chuyen_toi.png")

        # Hover over the "Ghim theo Tỷ lệ" option
        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Bên phải)')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_29_giao_dich__hover_ghim_ty_le.png")

        frame.locator("span:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_30_giao_dich__hover_duong.png")

        # Click on the "Thông tin Mã giao dịch" option
        frame.locator("span:has-text('Thông tin Mã giao dịch…')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_31_giao_dich__thong_tin_ma_giao_dich.png")

        # Close the "Thông tin Mã giao dịch" frame
        frame.locator("div.header-2ibjJG9Z span.close-2ibjJG9Z").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_32_giao_dich__dong_thong_tin_ma_giao_dich.png")

        # Click on the "Khối lượng" layer in the legend
        frame.locator("div.titleWrapper-2KhwsEwE:has-text('Khối lượng')").click()
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_33_giao_dich__an_layer_khoi_luong.png")

        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_34_giao_dich__hien_layer_khoi_luong.png")

        # Click on the settings icon for the "Khối lượng" layer
        frame.locator("[data-name='legend-settings-action']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_35_giao_dich__setting_khoi_luong.png")

        frame.locator("label:has-text('Dựa trên màu của phiên đóng cửa trước')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_36_giao_dich__checkbox_dong_cua_truoc.png")

        # Click on the "Định dạng" tab in the settings
        frame.locator("[data-name='tab-item-style']:has-text('Định dạng')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_37_giao_dich__tab_dinh_dang.png")

        # Click on the "Volume MA" checkbox to toggle it
        frame.locator("label:has-text('Volume MA')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_38_giao_dich__tick_volume_ma.png")

        # Click on the "Hiển thị" tab in the settings
        frame.locator("[data-name='tab-item-visibilities']:has-text('Hiển thị')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_39_giao_dich__tab_hien_thi.png")

        # Click on the "Tuần" checkbox to toggle it
        frame.locator("label:has-text('Tuần')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_40_giao_dich__tick_tuan.png")

        # Click on the "Các mặc định" button in the footer
        frame.locator("span#study-defaults-manager:has-text('Các mặc định')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_41_giao_dich__mac_dinh_setting_footer.png")

        # Click on the "OK" button in the "Các mặc định" modal
        frame.locator("span.submitButton-KW8170fm button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_42_giao_dich__xac_nhan_ok_khoi_luong.png")

        # Click on the "3 chấm" icon for the "Khối lượng" layer
        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_43_giao_dich__3_cham_layer_khoi_luong.png")

        # Hover over the "Thứ tự Trực quan" option
        frame.locator("span:has-text('Thứ tự Trực quan')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_44_giao_dich__hover_thu_tu_truc_quan_volume.png")

        # Hover over the "Chuyển tới" and "Ghim theo Tỷ lệ" options
        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_45_giao_dich__hover_chuyen_toi_volume.png")

        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Không có Tỷ lệ)')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_46_giao_dich__hover_ghim_volume.png")

        # Click on the "Sao chép" option in the "Khối lượng" layer settings
        frame.locator("span:has-text('Sao chép')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_47_giao_dich__remove_layer_volume.png")

        # Click on the "Xóa" option in the "Khối lượng" layer settings
        frame.locator("div.wrapper-1DJMiIgd").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_57_giao_dich__open_setting.png")

        frame.locator("span.label-f5BaKrKq:has-text('Nhãn')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_58_giao_dich__hover_nhan.png")

        frame.locator("span.label-f5BaKrKq:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_59_giao_dich__hover_duong.png")

        # Click on the "Đặt lại thang giá" option
        frame.locator("span.label-f5BaKrKq:has-text('Đặt lại thang giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_60_giao_dich__reset_scale.png")

        # Click on the "2w" timeframe option
        frame.locator("div.item-3SbREAgE:has-text('2w')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_61_2w.png")

        # Click on the "Mở cài đặt trục thời gian" option
        frame.locator("[data-name='go-to-date']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_62_giao_dich__open_time_axis_setting.png")

        # Click on the "Chọn ngày" button
        frame.locator("span[data-day='2025-08-01']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_63_giao_dich__chon_ngay_13.png")

        # Click on the "Phạm vi tùy chỉnh" tab
        frame.locator("[data-name='tab-item-customrange']:has-text('Phạm vi tùy chỉnh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_64_giao_dich__pham_vi_tuy_chinh.png")

        # Click on the "Từ" and "Đến" date pickers
        frame.locator("span[data-day='2025-07-10']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_65_giao_dich__chon_tu_ngay_13.png")

        frame.locator("span[data-day='2025-08-07']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_giao_dich__chon_den_ngay_13.png")

        frame.locator("span.submitButton-KW8170fm:has-text('Đến')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_1_giao_dich__chon_den_ngay_sau_click.png")

        # Click on the time zone dropdown
        frame.locator("[data-name='time-zone-menu']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_2_giao_dich__chon_mui_gio_dropdown.png")

        # Click on the "Denver" time zone option
        frame.locator("span:has-text('(UTC-6) Denver')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_67_giao_dich__chon_mui_gio_utc_denver.png")

        frame.locator("div.text-2Vpz_LXc:has-text('log')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_69_giao_dich__click_log.png")

        # Click on the "Tự động" button to toggle it
        frame.locator("div.text-2Vpz_LXc:has-text('tự động')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_70_giao_dich__click_tu_dong.png")

        # Interact with "Báo cáo phân tích" section
        self.page.locator("#tab-analysis-report").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_truy_cap.png")

        # Click on each report type and take screenshots
        self.page.locator("#filter-report-type").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_mo_dropdown.png")

        # Iterate through the report options and take screenshots
        options = ["filter-report-all", "filter-report-market", "filter-report-industry", "filter-report-macro", "filter-report-stock", "filter-report-other"]
        for i, option in enumerate(options, 1):
            self.page.locator(f"#{option}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"bao_cao_phantich_{option.lower().replace(' ', '_')}.png")
            if i < len(options):
                self.page.locator(f"#{option}").click()
                self.page.wait_for_timeout(1000)
                self.screenshot(f"bao_cao_phantich_mo_dropdown_{i}.png")

        # Click on the "Xem" button for the first report
        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_xem_1.png")

        # Close the modal after viewing the report
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_dong_modal_1.png")

        # Click on the "Xem" button for the second report
        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_xem_2.png")

        # Close the modal after viewing the second report
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_dong_modal_2.png")

    @allure.feature("Tìm kiếm mã chứng khoán")
    def capture_tab_search_and_subtabs(self):
        self.page.locator("#nav-pricing").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_khoi_dong.png")

        # Click on the search button to open the search dialog
        self.page.locator("button[aria-haspopup='dialog']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_mo_tim_kiem.png")

        # Fill in the search input with the stock code "PET"
        self.page.locator("input[aria-label='Tìm mã CK']").fill("PET")
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_nhap_ma.png")

        # Click on the search result for "PET"
        self.page.locator("div.font-bold:has-text('PET')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chon_ket_qua.png")

        # Click on the "Tổng quan" tab
        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tong_quan_1nam_ket_qua.png")

        # Click on the TA bot suggestions in turn
        self.page.locator("div.group:has(div:has-text('CCI Trend Confirmation'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_cci_trend.png")

        self.page.locator("div.group:has(div:has-text('Rolling Correlation Divergence'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_rolling_correlation.png")

        # Click on the TA bot suggestions in turn
        self.page.locator("div.group:has(div:has-text('Volume ROC Confirmation'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_roc.png")

        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Reversal'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_weighted_roc_reversal.png")

        # Click on the TA bot suggestions in turn
        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Crossover'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_weighted_roc_crossover.png")

        self.page.locator("div.group:has(div:has-text('ROC Breakout'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_roc_breakout.png")

        # Click on the "Bảng giá" tab
        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bang_gia.png")

        # Click on the "Biểu đồ" in subtabs "Bảng giá"
        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bang_gia_bieu_do.png")

        # Click on the "Nhận định" tab
        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_nhan_dinh.png")

        # Click on the "XChart AI" tab
        self.page.locator("#tab-xchart-ai").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_xchart_ai.png")

        # Select the time resolution and fill the date range
        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khung_thoi_gian.png")

        # Select the resolution option "15"
        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khung_thoi_gian_15.png")

        # Fill the date range inputs
        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khoang_thoi_gian.png")

        # Click on the "Load" button to load the chart data
        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("sau_khi_bam_nut_load.png")

        # Click on the "Chế độ hiển thị" dropdown to customize the chart display
        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("che_do_hien_thi_dropdown_mo.png")

        # Uncheck the "Chỉ hiện thị mô hình gần đây" option
        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("tuy_chinh_che_do_hien_thi_uncheck.png")

        # Check the "Hiển thị đường ZigZag" option
        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("tuy_chinh_che_do_hien_thi_check.png")

        # Select the number of forecast bars
        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_so_phien_du_bao.png")

        # Click on the "Biểu đồ RRG" button to view the RRG chart
        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bieu_do_rrg.png")

        #Click on the tabs in the RRG chart
        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"chon_tab_{label}.png")

        # Click on the "Thêm mã CK" button to add a stock code
        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_them_ma_ck.png")

        # Fill in the stock code input with "VCG"
        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_nhap_ma_VCG.png")

        # Click on the stock code "VCG" in the search results
        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_chon_ma_VCG.png")

        # Click on the "Thêm mã" button to add the stock code to the RRG chart
        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_thêm_ma_VCG.png")

        #Click on the tabs in the RRG chart again
        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"chon_tab_{label}.png")

        # Click on the "Dòng tiền thông minh" tab
        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_dong_tien_thong_minh.png")

        # Click on the "Tài chính" tab
        self.page.locator("#tab-finance").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tai_chinh.png")

        # Click on the "Chỉ số tài chính" button in the "Tài chính" tab
        self.page.locator("#subtab-finance-financial-metrics").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh.png")

        #Click on the "Phân tích nguồn vốn" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        # Click on the "Sức khoẻ tài chính" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Sức khoẻ tài chính").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        # Click on the "Tăng trưởng KQKD" tab in the "Chỉ số tài chính" section
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam.png")

        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        # Click on the "Phân tích nguồn vốn" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" tab in the "Chỉ số tài chính" section
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        # Click on the data tab in the "Chỉ số tài chính" section
        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tai_chinh_data.png")

        # Click on the "Hàng quý" button in the data
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_data_hang_quy.png")

        # Click on the "Báo cáo tài chính" tab
        self.page.locator("#subtab-finance-financial-reports").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh.png")

        #Click on the "Hàng năm" button in the "Báo cáo tài chính" section
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam.png")

        #Click on the data tab in the "Báo cáo tài chính" section
        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam_data.png")

        #Click on the "Hàng quý" button in the data of "Báo cáo tài chính"
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_data_hang_quy.png")

        #Click on the "Kết quả kinh doanh" tab
        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ket_qua_kinh_doanh.png")

        #Click on the "Hàng năm" button in the "Kết quả kinh doanh" section
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ket_qua_kinh_doanh_hang_quy.png")

        #Click on the "Lưu chuyển tiền tệ"
        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te.png")

        #Click on the "Hàng quý" button in the "Lưu chuyển tiền tệ" section
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te_hang_nam.png")

        # Click on the "Hồ sơ" tab
        self.page.locator("#tab-profile").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ho_so.png")

        # Click on the "Cổ đông & GD nội bộ" button
        self.page.locator("#subtab-profile-shareholders").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_co_dong_gd_noi_bo.png")

        # Close the modal
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_dong_modal.png")

    # Capture market tab and its subtabs
    @allure.feature("Thị trường")
    def capture_tab_thi_truong_and_subtabs(self):
        self.page.locator("#tab-market").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_1_thi_truong_bien_dong__phan_bo_dong_tien.png")
        print("[Captured] Biến động + Phân bổ dòng tiền")

        # Click on the "Biến động" button
        self.page.locator("#subtab-market-fluctuation-index-impact").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_2_thi_truong_tac_dong_index.png")
        print("[Captured] Tác động đến index")

        # Click on the "Nước ngoài" button
        self.page.locator("#subtab-market-foreign").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_3_thi_truong_nuoc_ngoai__1nam.png")
        print("[Captured] Nước ngoài - 1 năm")

        # Click on the "10 phiên" button in the "Nước ngoài" tab
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_4_thi_truong_nuoc_ngoai__10phien.png")
        print("[Captured] Nước ngoài - 10 phiên")

        # Click on the "Tự doanh" button
        self.page.locator("#subtab-market-proprietary").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_5_thi_truong_tu_doanh__ytd.png")
        print("[Captured] Tự doanh - YTD")

        # Click on the "10 phiên" button in the "Tự doanh" tab
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_6_thi_truong_tu_doanh__10phien.png")
        print("[Captured] Tự doanh - 10 phiên")

        # Click on the "Thanh khoản" button
        self.page.locator("#subtab-market-liquidity").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_7_thi_truong_thanh_khoan__5d.png")
        print("[Captured] Thanh khoản - 5D")

        # Click on the "0D" button in the "Thanh khoản" tab
        self.page.locator("button:has-text('0D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_8_thi_truong_thanh_khoan__0d.png")
        print("[Captured] Thanh khoản - 0D")

    # Capture stock tab and its subtabs
    @allure.feature("Cổ phiếu")
    def capture_tab_co_phieu_and_subtabs(self):

        self.page.locator("#tab-stocks").first.click()
        self.page.wait_for_timeout(2000)

        print("[Tab] CỔ PHIẾU > CHỈ SỐ")
        self.screenshot("7_1_co_phieu_chi_so__%.png")

        # click on the % to change the view
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_2_co_phieu_chi_so__thay_doi.png")

        # click on the GTGD to change the view
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_3_co_phieu_chi_so__klgd.png")

        # Click on the "Cổ phiếu" tab
        self.page.locator("#tab-stocks_subtab").click()
        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > CỔ PHIẾU > BÙNG NỔ KL")
        self.screenshot("7_4_bung_no_kl__1d_%.png")

        # Click on the % to change the view (1D- Bùng nổ KL)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_5_bung_no_kl__1d_thay_doi.png")

        # Click on the GTGD to change the view (1D- Bùng nổ KL)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_6_bung_no_kl__1d_gtgd.png")

        # Click on 5D
        self.page.locator("button:has-text('5D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_7_bung_no_kl__5d_%.png")

        # Click on the "Thay đổi" to change the view (5D- Bùng nổ KL)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_8_bung_no_kl__5d_thay_doi.png")

        # Click on the KLDG to change the view (5D- Bùng nổ KL)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_9_bung_no_kl__5d_gtgd.png")

        # Click on the "Biến động giá" in sublist "Cổ phiếu"
        self.page.locator("#subtab-stocks-price-fluctuation").click()
        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > BIẾN ĐỘNG GIÁ")
        self.screenshot("7_10_bien_dong__%.png")

        # Click on the "Thay đổi" to change the view
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_11_bien_dong__thay_doi.png")

        # Click on the "% 1W" to change the view
        self.page.locator("div.cursor-pointer:has-text('% 1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_12_bien_dong__1w.png")

        # Click on the "% 1M" to change the view
        self.page.locator("div.cursor-pointer:has-text('% 1M')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_13_bien_dong__1m.png")

        # Click on the "Cạn cung" in sublist "Cổ phiếu"
        self.page.locator("#subtab-stocks-low-supply").click()
        # self.page.locator("div.cursor-pointer:has-text('Cạn cung')").click()
        self.page.wait_for_timeout(2000)
        print("[Tab] CẠN CUNG")
        self.page.wait_for_timeout(2000)
        self.screenshot("7_14_can_cung_5d.png")

        # Click on the "Thay đổi" to change the view (5D- Cạn cung)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_15_can_cung__5d_thay_doi.png")

        # Click on the "KLGD" to change the view (5D- Cạn cung)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_16_can_cung_5d_gtgd.png")

        # Click on the "1D" button to change the view (1D- Cạn cung)
        self.page.locator("button:has-text('1D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_17_can_cung_1d_%.png")

        # Click on the "%" to change the view (1D- Cạn cung)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_18_can_cung_1d_thay_doi.png")

        # Click on the "KLGD" to change the view (1D- Cạn cung)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_19_can_cung__1d_klgd.png")

        # Click on the "Vượt đỉnh" in sublist "Cổ phiếu"
        self.page.locator("#subtab-stocks-breakout-high").click()
        # self.page.locator("div.cursor-pointer:has-text('Vượt đỉnh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_20_vuot_dinh__thay_doi.png")

        # Click on the "%" to change the view (Vượt đỉnh)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_21_vuot_dinh__%.png")

        # Click on the "GTGD" to change the view (Vượt đỉnh)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_22_vuot_dinh__gtgd.png")

        # Click on the "Phá đáy" in sublist "Cổ phiếu"
        self.page.locator("#subtab-stocks-breakout-low").click()
        # self.page.locator("div.cursor-pointer:has-text('Phá đáy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_23_pha_day__1d_%.png")

        # Click on the "%" to change the view (Phá đáy)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_24_pha_day__1d_thay_doi.png")

        # Click on the "KLGD" to change the view (Phá đáy)
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_25_pha_day__1d_klgd.png")

        # Click on the "Ngành" tab
        self.page.locator("button:has-text('Ngành')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_26_nganh.png")
        print("[Captured] Ngành")

    #Capture XBot AI tab and its subtabs
    @allure.feature("XBot AI")
    def capture_tab_xbot_ai_and_subtabs(self):

        self.page.locator("#tab-xbot-ai").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_1_xbot_tin_hieu__bot_phai_sinh.png")

        # Click on the "Bot cơ sở" button
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_2_xbot_tin_hieu__bot_co_so.png")

        # Click on the "Bot phái sinh" button
        self.page.locator("div.gap-3 button[data-key='botphaisinh']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_bot_phai_sinh.png")

        # Click on the "Nhận tín hiệu" button in the "Bot phái sinh" tab
        self.page.locator("div.gap-3 div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_3_modal_bot_phai_sinh__hieu_suat_1w.png")

        # Click on the "Tất cả" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Tất cả')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_4_modal_bot_phai_sinh__hieu_suat_tat_ca.png")

        # Click on the "Lệnh mở - Lịch sử" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_5_modal_bot_phai_sinh__lenh_mo_lich_su.png")

        # Click on the "Nhận tín hiệu" button in the modal
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_6_modal_xac_nhan_nhan_tin_hieu.png")

        # Click on the checkbox in the modal to confirm
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_7_modal_xac_nhan_da_tick_checkbox.png")

        # Click on the "Nhận tín hiệu" button to confirm
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_8_modal_sau_khi_xac_nhan_nhan_tin_hieu.png")

        # Close the modal after confirming
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_9_xbot__bot_phai_sinh_sau_nhan_tin_hieu.png")

        # Click on the "Bot cơ sở" button
        self.page.locator("div.gap-3 button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_bot_co_so.png")

        # Click on the "Nhận tín hiệu" button in the "Bot cơ sở" tab
        self.page.locator("div.gap-3 div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_10_modal_bot_co_so__hieu_suat_tat_ca.png")

        # Click on the "1W" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_11_modal_bot_co_so__hieu_suat_1w.png")

        # Click on the "Lệnh mở - Lịch sử" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_12_modal_bot_co_so__lenh_mo_lich_su.png")

        # Click on the "Nhận tín hiệu" button in the modal
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_13_modal_xac_nhan_bot_co_so.png")

        # Click on the checkbox in the modal to confirm
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_14_modal_bot_co_so__da_tick_checkbox.png")

        # Click on the "Nhận tín hiệu" button to confirm
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_15_modal_bot_co_so__sau_xac_nhan.png")

        # Close the modal after confirming
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_16_xbot__bot_co_so_sau_nhan_tin_hieu.png")

        # Search for a bot by code
        self.page.locator("input[placeholder*='Tìm bot theo mã']").fill("HAH")
        self.page.wait_for_timeout(2000)
        self.screenshot("8_17_xbot__tim_kiem_hah.png")

        # Click on the "Bot của tôi" button
        self.page.locator("div.gap-3 button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_21_xbot_bot_cua_toi__phai_sinh.png")

        # Click on the "Hủy nhận tín hiệu" button
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_22_xbot_bot_cua_toi__modal_huy_phai_sinh.png")

        # Confirm the cancellation in the modal
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_23_xbot_bot_cua_toi__phai_sinh_sau_huy.png")

        # Click on the "Bot cơ sở" button in the "Bot của tôi" tab
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_24_xbot_bot_cua_toi__co_so.png")

        # Click on the "Hủy nhận tín hiệu" button in the "Bot cơ sở" tab
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_25_xbot_bot_cua_toi__modal_huy_co_so.png")

        # Confirm the cancellation in the modal
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_26_xbot_bot_cua_toi__co_so_sau_huy.png")

    # Capture XBot TA tab and its subtabs
    @allure.feature("XBot TA")
    def capture_tab_xbot_ta_and_subtabs(self):
        self.page.locator("#tab-xbot-ta").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_xbot_ta.png")

    # Capture "Bang Gia" tab and its subtabs
    @allure.feature("Bảng giá")
    def capture_tab_bang_gia_and_subtabs_full(self):
        self.page.locator("#nav-pricing").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_1_bang_gia_tab.png")

        # CLick on the "Tất cả các ngành" dropdown to select industries
        self.page.locator("#industry-filter-button").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_2_nganh_hien_thi_dropdown.png")

        # Select "VN30" and "Thép" industries
        self.page.locator("label:has-text('VN30')").click()
        self.page.locator("label:has-text('Thép')").click()
        self.screenshot("9_2_1_bo_tick_vn30_thep.png")

        # view the selected industries
        self.page.mouse.click(0, 0)
        self.page.wait_for_timeout(1000)
        self.screenshot("9_3_bo_tick_vn30_thep.png")

        # Click on the "Thêm mã CK" button to add a stock code
        self.page.locator("#add-stock-button").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_4_modal_them_ma_ck.png")

        # Fill in the stock code input field with "TCB"
        self.page.locator("input[type='text']").fill("TCB")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_4_1_modal_them_ma_ck.png")

        # Click on the stock code "TCB" in the dropdown list
        self.page.locator("span:has-text('TCB')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_5_chon_TCB.png")

        # Click on the "Thêm mã" button to confirm adding the stock code
        self.page.locator("#confirm-add-stock-button").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_6_sau_khi_them_ma.png")

        # Click on the "TCB" stock code to open its modal
        self.page.locator("div[tabindex='0']:has-text('TCB')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_7_modal_TCB_tong_quan.png")

        # Click on the "1 năm" button in the modal
        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_7_1_modal_TCB_tong_quan_1nam.png")

        # Click on the "Bảng giá" button in the modal
        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_8_modal_TCB_nhan_dinh.png")

        # Click on the bieudo button in the subtabs "Bảng giá"
        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_9_modal_TCB_bieu_do.png")

        # Click on the "Nhận định" button in the modal
        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_10_modal_evf_nhan_dinh.png")

        # Click on the "XChart AI" tab in the modal
        self.page.locator("#tab-xchart-ai").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_11_xchart_ai_tab.png")

        # Select the time resolution and fill the date range
        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_1_chon_khung_thoi_gian.png")

        # Select "15 phút" resolution
        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_2chon_khung_thoi_gian_15.png")

        # Fill the date range for the chart
        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_3_chon_khoang_thoi_gian.png")

        # Click on the "Load" button to load the chart data
        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_4_sau_khi_bam_nut_load.png")

        # Click on the "Chế độ hiển thị" dropdown to customize the display mode
        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_5_che_do_hien_thi_dropdown_mo.png")

        # Uncheck the "Chỉ hiện thị mô hình gần đây" option
        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_6_tuy_chinh_che_do_hien_thi_uncheck.png")

        # Check the "Hiện thị ZigZag" option
        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_7_tuy_chinh_che_do_hien_thi_check.png")

        # Select the number of forecast bars to display
        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_8_chon_so_phien_du_bao.png")

        # CLick on the "Biểu đồ RRG" button in the modal
        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_rrg_1d.png")

        # Click on the tabs in the RRG chart
        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"9_13_1_chon_tab_{label}.png")

        # Click on the "Thêm mã CK" button in the RRG chart
        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13__2Bieu_do_RRG_them_ma_ck.png")

        # Fill in the stock code input field with "VCG"
        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_3_Bieu_do_RRG_nhap_ma_VCG.png")

        # Click on the stock code "VCG" in the dropdown list
        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_4_Bieu_do_RRG_chon_ma_VCG.png")

        # Click on the "Thêm mã" button to confirm adding the stock code in the RRG chart
        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_5_Bieu_do_RRG_thêm_ma_VCG.png")

        # Click on the tabs in the RRG chart again
        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"9_13_6_chon_tab_{label}.png")

        # Click on the "Dòng tiền thông minh" button
        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_14_dong_tien_thong_minh.png")

        # Click on the "Tài chính" button in the modal
        self.page.locator("#tab-finance").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_15_tai_chinh_dinh_gia.png")

        # Click on the "Chỉ số tài chính" button
        self.page.locator("#subtab-finance-financial-metrics").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_16_chi_so_quy_kqkd.png")

        # Click on the "Phân tích nguồn vốn" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_1_tim_kiem_pet_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_2_tim_kiem_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_3_tim_kiem_pet_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        # Click on the "Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_4_tim_kiem_pet_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        # Click on the "Hàng năm" in subtabs "Chỉ số tài chính"
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_17_chi_so_nam_mac_dinh.png")

        # Click on the "Tăng trưởng KQKD" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_1_tim_kiem_pet_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        # Click on the "Phân tích nguồn vốn" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_2_tim_kiem_pet_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_3_tim_kiem_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" button in subtabs "Chỉ số tài chính"
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_4_tim_kiem_pet_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        # Click on the data-key=data button in subtabs "Chỉ số tài chính"
        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_5_tim_kiem_pet_tai_chinh_data.png")

        # Click on the "Hàng quý" in subtabs "Chỉ số tài chính"
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_6_tim_kiem_pet_chi_so_tai_chinh_data_hang_quy.png")

        # Click on the "Báo cáo tái chính" button
        self.page.locator("#subtab-finance-financial-reports").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_19_bao_cao_cdkh_quy.png")

        # Click on the "Hàng naăm" in subtabs "Báo cáo tài chính"
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_20_bao_cao_cdkh_nam.png")

        # Click on the "Kết quả kinh doanh" button
        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_21_kqkd_nam.png")

        # Click on the "Hàng quý" in subtabs "Kết quả kinh doanh"
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_22_kqkd_quy.png")

        # Click on the "Lưu chuyển tiền tệ" button
        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_23_luu_chuyen_quy.png")

        # Click on the "Hàng năm" in subtabs "Lưu chuyển tiền tệ"
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_24_luu_chuyen_nam.png")

        # Click on the "Hồ sơ" tab
        self.page.locator("#tab-profile").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_25_ho_so_cong_ty.png")

        # Click on the "Cổ đông & GD nội bộ" button in the "Hồ sơ" tab
        self.page.locator("#subtab-profile-shareholders").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_26_ho_so_co_dong.png")

        # Close the modal
        self.page.locator("button[aria-label='Close']").click()

    # Capture "San Bot" tab and its subtabs
    @allure.feature("Sàn bot")
    def capture_tab_san_bot_and_subtabs(self):
        self.page.locator("#nav-bot-platform").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot.png")

        # Click on the "Nhận tín hiệu" button in the "Bot phái sinh" tab
        self.page.locator("div.bg-card.rounded-full div.text-xs:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_nhan_tin_hieu_phai_sinh.png")

        # Click on the "Tất cả" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Tất cả')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_tat_ca.png")

        # Click on the "Lệnh mở - Lịch sử" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_lenh_mo_lich_su_phai_sinh.png")

        # Click on the "Nhận tín hiệu" button in the modal
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_phai_sinh_1.png")

        # Click on the checkbox in the modal to confirm
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tick_checkbox_phai_sinh.png")

        # Click on the "Nhận tín hiệu" button to confirm
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_phai_sinh_2.png")

        # Close the modal after confirming
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_dong_modal_phai_sinh1.png")

        # Click on the "Bot cơ sở" button
        self.page.locator("button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_co_so.png")

        # Click on the "Nhận tín hiệu" button in the "Bot cơ sở" tab
        self.page.locator("div.bg-card.rounded-full div.text-xs:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_nhan_tin_hieu_co_so.png")

        # Click on the "1W" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_1w_co_so.png")

        # Click on the "Lệnh mở - Lịch sử" tab in the modal
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_lenh_mo_lich_su_co_so.png")

        # Click on the "Nhận tín hiệu" button in the modal
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_co_so_1.png")

        # Click on the checkbox in the modal to confirm
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tick_checkbox_co_so.png")

        # Click on the "Nhận tín hiệu" button to confirm
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_co_so_2.png")

        # Close the modal after confirming
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_dong_modal_co_so1.png")

        # Click on the "Bot của tôi" button
        self.page.locator("button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_cua_toi_phai_sinh.png")

        # Click on the "Hủy nhận tín hiệu" button
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_huy_tin_hieu_phai_sinh.png")

        # Confirm the cancellation in the modal
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_huy_phai_sinh.png")

        # Click on the "Bot cơ sở" button in the "Bot của tôi" tab
        self.page.wait_for_selector("button[data-key='$.1']", state="visible", timeout=30000)
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_cua_toi_co_so.png")

        # Click on the "Hủy nhận tín hiệu" button in the "Bot cơ sở" tab
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_huy_tin_hieu_co_so.png")

        # Confirm the cancellation in the modal
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_huy_co_so.png")

    # Capture "Goi Dich Vu" tab and its subtabs
    @allure.feature("Gói dịch vụ")
    def capture_tab_goi_dich_vu_and_subtabs(self):
        self.page.locator("a:has-text('Gói dịch vụ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("goi_dich_vu.png")

    # Capture "Loc Co Phieu" tab and its subtabs
    @allure.feature("Lọc cổ phiếu")
    def capture_tab_loc_stock_and_subtabs(self):
        # Click on the "Lọc cổ phiếu" tab
        self.page.locator("#nav-stock-filter").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot.png")

        # Click on the "Cổ phiếu tăng trưởng"
        self.page.locator("#filter-growth-stocks").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tang_truong_1.png")

        # Click on the "Cổ phiếu xu hướng mạnh"
        self.page.locator("#filter-value-stocks").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri.png")

        # Click on the "Cổ phiếu phục hồi"
        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu phục hồi')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_phuc_hoi.png")

        # Click on the "Cổ phiếu giá trị"
        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu giá trị')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri.png")

        # Click on the "Nhóm biến động giá"
        self.page.locator("#group-price-volatility").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhom_bien_dong_gia.png")

        # Click on the "Nhóm thông dụng"
        self.page.locator("#group-common").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhom_thong_dung.png")

        # Click on the "Giá trị giao dịch trung bình 50 phiên (tỷ)"
        self.page.locator("#filter-avg-transaction-value-50").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri_gd_50_phien.png")

        # Click on the "Giá trị giao dịch (tỷ)"
        self.page.locator("#filter-transaction-value").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri_gd.png")

        # Click on the stock code "BID"
        self.page.locator("div.font-semibold:has-text('BID')").first.click()
        self.page.wait_for_url("https://xno.vn/loc-co-phieu?symbol=BID&chiTietMaCK=true", timeout=20000)
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ma_bid.png")

        # Click on the "1 năm" in "Tổng quan" tab
        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ma_bid_tong_quan_1nam_ket_qua.png")

        # Click on the subtabs "Bảng giá" in "Tổng quan" tab
        self.page.locator("button[data-key='banggia']:has-text('Bảng giá')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bang_gia.png")

        # Click on the "Biểu đồ" in subtabs "Bảng giá"
        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bang_gia_bieu_do.png")

        # Click on the subtabs "Nhận định" in "Tổng quan" tab
        self.page.locator("button[data-key='nhandinh']:has-text('Nhận định')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhan_dinh.png")

        # Click on the "XChart AI" tab
        self.page.locator("#tab-xchart-ai").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_xchart_ai.png")

        # Select the time resolution and fill the date range
        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khung_thoi_gian.png")

        # Select the 15-minute resolution
        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khung_thoi_gian_15.png")

        # Fill the date range for the chart
        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khoang_thoi_gian.png")

        # Click on the "Load" button to load the chart data
        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_sau_khi_bam_nut_load.png")

        # Click on the "Chế độ hiển thị" dropdown to customize the chart display
        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_che_do_hien_thi_dropdown_mo.png")

        # Uncheck the "Chỉ hiện thị mô hình gần đây" option
        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tuy_chinh_che_do_hien_thi_uncheck.png")

        # Check the "Hiển thị đường ZigZag" option
        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tuy_chinh_che_do_hien_thi_check.png")

        # Select the number of forecast bars
        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_so_phien_du_bao.png")

        # Click on the "Biểu đồ RRG" button to view the RRG chart
        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bieu_do_rrg.png")

        # Click on the tabs in the RRG chart
        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"loc_co_phieu_chon_tab_{label}.png")

        # Click on the "Thêm mã CK" button in the RRG chart
        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_them_ma_ck.png")

        # Fill the stock code input with "VCG"
        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_nhap_ma_VCG.png")

        # Click on the stock code "VCG" in the suggestions
        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_chon_ma_VCG.png")

        # Click on the "Thêm mã" button to add the stock code to the RRG chart
        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_thêm_ma_VCG.png")

        # Click on the tabs in the RRG chart again
        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"loc_co_phieu_chon_tab_{label}.png")

        # Click on the "Dòng tiền thông minh" button
        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_dong_tien_thong_minh.png")

        # Click on the "Tài chính" button
        self.page.locator("button[data-key='phantichtaichinh']:has-text('Tài chính')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tai_chinh.png")

        # Click on the "Chỉ số tài chính" button in the "Tài chính" tab
        self.page.locator("#subtab-finance-financial-metrics").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh.png")

        # Click on the "Phân tích nguồn vốn" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        # Click on the "Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        # Click on the "Hàng năm" button in the "Chỉ số tài chính" tab
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam.png")

        # Click on the "Tăng trưởng KQKD" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        # Click on the "Phân tích nguồn vốn" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        # Click on the "Phân tích tài sản" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        # Click on the "Hiệu quả sinh lời" tab in the "Chỉ số tài chính" tab
        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        # Click on the "Data" button in the "Chỉ số tài chính" tab
        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tai_chinh_data.png")

        # Click on the "Hàng quý" button in the "Data" tab
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_data_hang_quy.png")

        # Click on the "Báo cáo tài chính" button
        self.page.locator("#subtab-finance-financial-reports").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu__bao_cao_tai_chinh.png")

        # Click on the "Hàng năm" button in the "Báo cáo tài chính" tab
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam.png")

        # Click on the "Kết quả kinh doanh" button
        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ket_qua_kinh_doanh.png")

        # Click on the "Hàng quý" button in the "Kết quả kinh doanh" tab
        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ket_qua_kinh_doanh_hang_quy.png")

        # Click on the "Lưu chuyển tiền tệ" button
        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te.png")

        # Click on the "Hàng năm" button in the "Lưu chuyển tiền tệ" tab
        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te_hang_nam.png")

        # Click on the "Hồ sơ" button# Click on the "Hồ sơ" button
        self.page.locator("button[data-key='thongtindoanhnghiep']:has-text('Hồ sơ')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ho_so.png")

        # Click on the "Cổ đông & GD nội bộ" button in the "Hồ sơ" tab
        self.page.locator("#subtab-profile-shareholders").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_co_dong_gd_noi_bo.png")

        # Close the modal
        self.page.locator("button[aria-label='Close']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_dong_modal.png")

    # Capture "Thong Tin Ca Nhan" tab and its subtabs
    @allure.feature("Thông tin cá nhân")
    def capture_tab_thong_tin_and_subtabs(self):
        self.page.locator('button span[role="img"] svg').nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Thong_bao")

        # Capture the light mode toggle
        self.page.locator('button span[role="img"] svg').nth(2).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bat_che_do_sang")

        # Toggle the dark  mode again
        self.page.locator('button span[role="img"] svg').nth(2).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Tat_che_do_sang")

        # Click on the user profile icon to access personal information
        self.page.locator("span[data-slot='trigger'][aria-haspopup='true']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan.png")

        # Click on the "Thông tin cá nhân" tab
        self.page.locator("li[data-key='user-info']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Vao_trang_thong_tin_ca_nhan.png")

        # Click on the "Mật khẩu" button
        self.page.locator("div.flex.cursor-pointer:has-text('Mật khẩu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan_mat_khau.png")

        # Click on the "Gói hội viên" button
        self.page.locator("div.flex.cursor-pointer:has-text('Gói hội viên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan_goi_hoi_vien.png")

        # Click on the "Đăng xuất" button
        self.page.locator("span[data-slot='trigger'][aria-haspopup='true']").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("li[data-key='dang-xuat']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Vao_trang_thong_tin_ca_nhan.png")