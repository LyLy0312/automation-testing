import os
import allure
from playwright.sync_api import Page
from utils.decorators import screenshot_decorator

class XNODashboardPageDirect:
    def __init__(self, page: Page):
        self.page = page

    @screenshot_decorator
    def screenshot(self, name: str):
        pass

    def wait_and_capture(self, url: str, selector: str, filename: str):
        self.page.goto(url)
        self.page.wait_for_selector(selector, timeout=10000)
        self.page.wait_for_timeout(2000)
        self.screenshot(path=os.path.join("../..", "screenshots", filename), full_page=True)
        print(f"[Captured] {filename}")

    @allure.feature("Main Tabs")
    def capture_main_tabs(self):
        main_tabs = [
            ("https://xno.vn/giao-dich", "a[href='/giao-dich?']", "1_giao_dich.png"),
            ("https://xno.vn/bang-gia", "a[href='/bang-gia?']", "2_bang_gia.png"),
            ("https://xno.vn/loc-co-phieu", "a[href='/loc-co-phieu?']", "3_loc_co_phieu.png"),
            ("https://xno.vn/goi-dich-vu", "a[href='/goi-dich-vu?']", "4_goi_dich_vu.png"),
            ("https://xno.vn/san-bot", "div.flex.items-center.gap-3", "5_san_bot.png"),
        ]
        for url, selector, filename in main_tabs:
            self.wait_and_capture(url, selector, filename)

    @allure.feature("Giao dịch")
    def capture_tab_giao_dich_and_subtabs(self):
        self.page.wait_for_timeout(2000)
        self.screenshot("0_1_giao_dich_bieu_do_mac_dinh.png")

        frame = self.page.frame_locator("iframe[src*='vi-tv-chart']")
        frame.locator("#header-toolbar-intervals div[data-role='button'] .value-2y-wa9jT", has_text="D").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_1_giao_dich__dropdown_timeframe.png")

        frame.locator("div[data-value='1W']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_2_giao_dich__chon_timeframe_1w.png")

        frame.locator("#header-toolbar-chart-styles div[data-role='button'][title*='Biểu đồ']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_3_giao_dich__dropdown_kieu_bieu_do.png")

        frame.locator("div[data-value='bar']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_4_giao_dich__chon_kieu_bieu_do_hinh_thanh.png")

        frame.locator("#header-toolbar-indicators div[data-role='button']:has-text('Các chỉ báo')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_giao_dich__dropdown_chi_bao.png")

        frame.locator("span:has-text('Aroon')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_1_Aroon.png")

        frame.locator("span:has-text('Biến động Chaikin')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_2_ Biến đôộng chaikin.png")

        frame.locator("input[placeholder*='Tìm kiếm']").fill("TRIX")
        self.page.wait_for_timeout(2000)
        self.screenshot("1_5_3_ Tìm kiếm.png")

        frame.locator("span:has-text('TRIX')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_6_giao_dich__chon_chi_bao_trix.png")

        frame.locator("span[data-role='button'][data-name='close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_7_giao_dich__sau_khi_chon_chi_bao.png")

        frame.locator("div[data-role='button'].buttonUndo-nGqa616C").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_8_giao_dich__khoi_phuc_chi_bao.png")

        redo_button = frame.locator("div[data-role='button'].buttonUndo-nGqa616C").nth(1)

        if redo_button.is_visible() and "isDisabled" not in (redo_button.get_attribute("class") or ""):
            redo_button.click()
        else:
            print("Redo button is either hidden or disabled.")
        self.page.wait_for_timeout(2000)
        self.screenshot("1_9_giao_dich__hien_lai_chi_bao.png")

        frame.locator("#header-toolbar-properties").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_10_giao_dich__mo_modal_cai_dat.png")

        frame.locator("span.titleText-DggvOZTm:has-text('Mã')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_11_Mã.png")

        frame.locator("label:has-text('Các Thanh màu Dựa trên giá Đóng cửa Phiên trước')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_11_1_giao_dich__cai_dat_tab_ma_tick_checkbox.png")

        frame.locator("span.titleText-DggvOZTm:has-text('Dòng trạng thái')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_12_giao_dich__cai_dat_tab_dong_trang_thai.png")

        frame.locator("div[data-section-name='symbolTextSource'] [data-role='listbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_13_giao_dich__cai_dat_dropdown_mo_ta.png")

        frame.locator("div[role='option']:has-text('Ticker')").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_14_giao_dich__cai_dat_mo_ta_chon_ticker.png")

        frame.locator("span.titleText-DggvOZTm:has-text('Các tỷ lệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_Cac-ti-lệ.png")

        # Bật checkbox "Biểu tượng Nhãn tên"
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_1_giao_dich__bieu_tuong_nhan_ten_checked.png")

        # Tắt checkbox (nếu cần)
        frame.locator("label:has-text('Biểu tượng Nhãn tên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_15_2_giao_dich__bieu_tuong_nhan_ten_unchecked.png")

        frame.locator("span.titleText-DggvOZTm:has-text('Diện mạo')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_16_giao_dich__tab_dien_mao.png")

        frame.locator("span[data-role='listbox'][data-name='background-type-options-dropdown']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_17_giao_dich__chon_hinh_nen_dropdown.png")

        frame.locator("div[role='option']:has-text('Gradient')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_18_giao_dich__chon_gradient.png")

        frame.locator("button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_19_giao_dich__sau_khi_xac_nhan_modal_cai_dat.png")

        frame.locator("#header-toolbar-screenshot").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_20_giao_dich__icon_chup_anh.png")

        frame.locator("div[data-name='save-chart-image']:has-text('Lưu hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_21_giao_dich__luu_hinh_anh_bieu_do.png")

        frame.locator("#header-toolbar-screenshot").click()
        frame.locator("div[data-name='copy-chart-image']:has-text('Sao chép hình ảnh biểu đồ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_22_giao_dich__sao_chep_hinh_anh_bieu_do.png")

        frame.locator("div[data-name='legend-source-title']:has-text('VNINDEX')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_23_giao_dich__thanh_ngang_vnindex1w.png")

        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_24_giao_dich__an_layer_vnindex1w.png")

        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_25_giao_dich__hien_layer_vnindex1w.png")

        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_26_giao_dich__3_cham_layer_vnindex1w.png")

        frame.locator("span:has-text('Thứ tự trực quan')").first.hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_27_giao_dich__hover_thu_tu_truc_quan.png")

        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_28_giao_dich__hover_chuyen_toi.png")

        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Bên phải)')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_29_giao_dich__hover_ghim_ty_le.png")

        frame.locator("span:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_30_giao_dich__hover_duong.png")

        frame.locator("span:has-text('Thông tin Mã giao dịch…')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_31_giao_dich__thong_tin_ma_giao_dich.png")

        frame.locator("div.header-2ibjJG9Z span.close-2ibjJG9Z").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_32_giao_dich__dong_thong_tin_ma_giao_dich.png")

        frame.locator("div.titleWrapper-2KhwsEwE:has-text('Khối lượng')").click()
        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_33_giao_dich__an_layer_khoi_luong.png")

        frame.locator("[data-name='legend-show-hide-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_34_giao_dich__hien_layer_khoi_luong.png")

        frame.locator("[data-name='legend-settings-action']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_35_giao_dich__setting_khoi_luong.png")

        frame.locator("label:has-text('Dựa trên màu của phiên đóng cửa trước')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_36_giao_dich__checkbox_dong_cua_truoc.png")

        frame.locator("[data-name='tab-item-style']:has-text('Định dạng')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_37_giao_dich__tab_dinh_dang.png")

        frame.locator("label:has-text('Volume MA')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_38_giao_dich__tick_volume_ma.png")

        frame.locator("[data-name='tab-item-visibilities']:has-text('Hiển thị')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_39_giao_dich__tab_hien_thi.png")

        frame.locator("label:has-text('Tuần')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_40_giao_dich__tick_tuan.png")

        frame.locator("span#study-defaults-manager:has-text('Các mặc định')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_41_giao_dich__mac_dinh_setting_footer.png")

        frame.locator("span.submitButton-KW8170fm button:has-text('OK')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_42_giao_dich__xac_nhan_ok_khoi_luong.png")

        frame.locator("[data-name='legend-more-action'] .buttonIcon-2KhwsEwE").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_43_giao_dich__3_cham_layer_khoi_luong.png")

        frame.locator("span:has-text('Thứ tự Trực quan')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_44_giao_dich__hover_thu_tu_truc_quan_volume.png")

        frame.locator("span:has-text('Chuyển tới')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_45_giao_dich__hover_chuyen_toi_volume.png")

        frame.locator("span:has-text('Ghim theo Tỷ lệ (Hiện tại Không có Tỷ lệ)')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_46_giao_dich__hover_ghim_volume.png")

        frame.locator("span:has-text('Sao chép')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_47_giao_dich__remove_layer_volume.png")


        frame.locator("div.wrapper-1DJMiIgd").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_57_giao_dich__open_setting.png")

        frame.locator("span.label-f5BaKrKq:has-text('Nhãn')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_58_giao_dich__hover_nhan.png")

        frame.locator("span.label-f5BaKrKq:has-text('Đường')").hover()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_59_giao_dich__hover_duong.png")

        frame.locator("span.label-f5BaKrKq:has-text('Đặt lại thang giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_60_giao_dich__reset_scale.png")

        frame.locator("div.item-3SbREAgE:has-text('2w')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_61_2w.png")

        frame.locator("[data-name='go-to-date']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_62_giao_dich__open_time_axis_setting.png")

        frame.locator("span[data-day='2025-08-01']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_63_giao_dich__chon_ngay_13.png")

        frame.locator("[data-name='tab-item-customrange']:has-text('Phạm vi tùy chỉnh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_64_giao_dich__pham_vi_tuy_chinh.png")

        frame.locator("span[data-day='2025-07-10']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_65_giao_dich__chon_tu_ngay_13.png")

        frame.locator("span[data-day='2025-08-07']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_giao_dich__chon_den_ngay_13.png")

        frame.locator("span.submitButton-KW8170fm:has-text('Đến')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_1_giao_dich__chon_den_ngay_sau_click.png")

        frame.locator("[data-name='time-zone-menu']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_66_2_giao_dich__chon_mui_gio_dropdown.png")

        frame.locator("span:has-text('(UTC-6) Denver')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_67_giao_dich__chon_mui_gio_utc_denver.png")

        frame.locator("div.text-2Vpz_LXc:has-text('log')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_69_giao_dich__click_log.png")

        frame.locator("div.text-2Vpz_LXc:has-text('tự động')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("1_70_giao_dich__click_tu_dong.png")

        self.page.locator("button[data-key='baocaophantich']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_truy_cap.png")

        self.page.locator("button[aria-haspopup='listbox']:has(span:text('Loại báo cáo'))").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_mo_dropdown.png")

        options = ["Tất cả", "Báo cáo Thị Trường", "Báo cáo Ngành", "Báo cáo Vĩ mô", "Cổ phiếu", "Khác"]
        for i, option in enumerate(options, 1):
            self.page.locator(f"li[role='option']:has(span:text('{option}'))").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"bao_cao_phantich_{option.lower().replace(' ', '_')}.png")
            if i < len(options):
                self.page.locator(f"button[aria-haspopup='listbox']:has(span:text('{option}'))").click()
                self.page.wait_for_timeout(1000)
                self.screenshot(f"bao_cao_phantich_mo_dropdown_{i}.png")

        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_xem_1.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_dong_modal_1.png")

        self.page.locator("div.cursor-pointer.text-right:has-text('Xem')").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("bao_cao_phantich_xem_2.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("bao_cao_phantich_dong_modal_2.png")

    @allure.feature("Tìm kiếm mã chứng khoán")
    def capture_tab_search_and_subtabs(self):
        self.page.locator("a:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_khoi_dong.png")

        self.page.locator("button[aria-haspopup='dialog']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_mo_tim_kiem.png")

        self.page.locator("input[aria-label='Tìm mã CK']").fill("PET")
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_nhap_ma.png")

        self.page.locator("div.font-bold:has-text('PET')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chon_ket_qua.png")

        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tong_quan_1nam_ket_qua.png")

        self.page.locator("div.group:has(div:has-text('CCI Trend Confirmation'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_cci_trend.png")

        self.page.locator("div.group:has(div:has-text('Rolling Correlation Divergence'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_rolling_correlation.png")

        self.page.locator("div.group:has(div:has-text('Volume ROC Confirmation'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_roc.png")

        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Reversal'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_weighted_roc_reversal.png")

        self.page.locator("div.group:has(div:has-text('Volume Weighted ROC Crossover'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_volume_weighted_roc_crossover.png")

        self.page.locator("div.group:has(div:has-text('ROC Breakout'))").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_roc_breakout.png")

        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bang_gia.png")

        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bang_gia_bieu_do.png")

        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_nhan_dinh.png")

        self.page.locator("button:has-text('XChart AI')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_xchart_ai.png")

        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khung_thoi_gian.png")

        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khung_thoi_gian_15.png")

        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_khoang_thoi_gian.png")

        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("sau_khi_bam_nut_load.png")

        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("che_do_hien_thi_dropdown_mo.png")

        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("tuy_chinh_che_do_hien_thi_uncheck.png")

        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("tuy_chinh_che_do_hien_thi_check.png")

        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("chon_so_phien_du_bao.png")

        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bieu_do_rrg.png")

        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"chon_tab_{label}.png")

        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_them_ma_ck.png")

        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_nhap_ma_VCG.png")

        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_chon_ma_VCG.png")

        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bieu_do_RRG_thêm_ma_VCG.png")

        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"chon_tab_{label}.png")

        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_dong_tien_thong_minh.png")

        self.page.locator("button:has-text('Tài chính')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tai_chinh.png")

        self.page.locator("button:has-text('Chỉ số tài chính')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        self.page.locator("div.flex >> text=Sức khoẻ tài chính").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam.png")

        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_tai_chinh_data.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_chi_so_tai_chinh_data_hang_quy.png")

        self.page.locator("button:has-text('Báo cáo tài chính')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam.png")

        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam_data.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_data_hang_quy.png")

        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ket_qua_kinh_doanh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ket_qua_kinh_doanh_hang_quy.png")

        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te_hang_nam.png")

        self.page.locator("button:has-text('Hồ sơ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_ho_so.png")

        self.page.locator("button:has-text('Cổ đông & GD nội bộ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_co_dong_gd_noi_bo.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_dong_modal.png")

    @allure.feature("Thị trường")
    def capture_tab_thi_truong_and_subtabs(self):
        self.page.locator("button:has-text('Thị trường')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_1_thi_truong_bien_dong__phan_bo_dong_tien.png")
        print("[Captured] Biến động + Phân bổ dòng tiền")

        self.page.locator("button:has-text('Tác động đến index')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_2_thi_truong_tac_dong_index.png")
        print("[Captured] Tác động đến index")

        self.page.locator("button:has-text('Nước ngoài')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_3_thi_truong_nuoc_ngoai__1nam.png")
        print("[Captured] Nước ngoài - 1 năm")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_4_thi_truong_nuoc_ngoai__10phien.png")
        print("[Captured] Nước ngoài - 10 phiên")

        self.page.locator("button:has-text('Tự doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_5_thi_truong_tu_doanh__ytd.png")
        print("[Captured] Tự doanh - YTD")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_6_thi_truong_tu_doanh__10phien.png")
        print("[Captured] Tự doanh - 10 phiên")

        self.page.locator("button:has-text('Thanh khoản')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_7_thi_truong_thanh_khoan__5d.png")
        print("[Captured] Thanh khoản - 5D")
        self.page.locator("button:has-text('0D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("6_8_thi_truong_thanh_khoan__0d.png")
        print("[Captured] Thanh khoản - 0D")

    @allure.feature("Cổ phiếu")
    def capture_tab_co_phieu_and_subtabs(self):

        self.page.locator("button:has-text('Cổ phiếu')").first.click()
        self.page.wait_for_timeout(2000)

        print("[Tab] CỔ PHIẾU > CHỈ SỐ")
        self.screenshot("7_1_co_phieu_chi_so__%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_2_co_phieu_chi_so__thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_3_co_phieu_chi_so__klgd.png")

        self.page.locator("div[data-slot='tabContent']:text('Cổ phiếu')").click()

        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > CỔ PHIẾU > BÙNG NỔ KL")

        self.screenshot("7_4_bung_no_kl__1d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_5_bung_no_kl__1d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_6_bung_no_kl__1d_gtgd.png")

        self.page.locator("button:has-text('5D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_7_bung_no_kl__5d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_8_bung_no_kl__5d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_9_bung_no_kl__5d_gtgd.png")

        self.page.locator("div.flex >> text=Biến động giá").click()

        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > BIẾN ĐỘNG GIÁ")

        self.screenshot("7_10_bien_dong__%.png")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_11_bien_dong__thay_doi.png")

        self.page.locator("div.cursor-pointer:has-text('% 1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_12_bien_dong__1w.png")

        self.page.locator("div.cursor-pointer:has-text('% 1M')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_13_bien_dong__1m.png")

        self.page.locator("div.flex >> text=Cạn cung").click()
        # self.page.locator("div.cursor-pointer:has-text('Cạn cung')").click()
        self.page.wait_for_timeout(2000)
        print("[Tab] CẠN CUNG")

        self.screenshot("7_15_can_cung__1d_%.png")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()

        self.page.wait_for_timeout(2000)
        self.screenshot("7_14_can_cung__1d_thay_doi.png")


        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_16_can_cung__1d_gtgd.png")

        self.page.locator("button:has-text('1D')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_17_can_cung__5d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_18_can_cung__5d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_19_can_cung__5d_klgd.png")

        self.page.locator("div.flex >> text=Vượt đỉnh").click()
        # self.page.locator("div.cursor-pointer:has-text('Vượt đỉnh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_20_vuot_dinh__thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_21_vuot_dinh__%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_22_vuot_dinh__gtgd.png")

        self.page.locator("div.flex >> text=Phá đáy").click()
        # self.page.locator("div.cursor-pointer:has-text('Phá đáy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_23_pha_day__1d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_24_pha_day__1d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("7_25_pha_day__1d_klgd.png")

        # self.page.locator("button:has-text('Ngành')").click()
        self.page.locator("div[data-slot='tabContent']:text('Ngành')").click()

        self.page.wait_for_timeout(2000)
        self.screenshot("7_26_nganh.png")
        print("[Captured] Ngành")

    @allure.feature("XBot AI")
    def capture_tab_xbot_ai_and_subtabs(self):

        self.page.locator("button:has-text('XBot AI')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_1_xbot_tin_hieu__bot_phai_sinh.png")

        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_2_xbot_tin_hieu__bot_co_so.png")

        self.page.locator("div.gap-3 button[data-key='botphaisinh']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_bot_phai_sinh.png")

        self.page.locator("div.gap-3 div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_3_modal_bot_phai_sinh__hieu_suat_1w.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Tất cả')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_4_modal_bot_phai_sinh__hieu_suat_tat_ca.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_5_modal_bot_phai_sinh__lenh_mo_lich_su.png")

        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_6_modal_xac_nhan_nhan_tin_hieu.png")

        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_7_modal_xac_nhan_da_tick_checkbox.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_8_modal_sau_khi_xac_nhan_nhan_tin_hieu.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_9_xbot__bot_phai_sinh_sau_nhan_tin_hieu.png")

        self.page.locator("div.gap-3 button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_bot_co_so.png")

        self.page.locator("div.gap-3 div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_10_modal_bot_co_so__hieu_suat_tat_ca.png")

        self.page.locator("div[data-slot='tabContent']:has-text('1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_11_modal_bot_co_so__hieu_suat_1w.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_12_modal_bot_co_so__lenh_mo_lich_su.png")

        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_13_modal_xac_nhan_bot_co_so.png")

        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_14_modal_bot_co_so__da_tick_checkbox.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_15_modal_bot_co_so__sau_xac_nhan.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_16_xbot__bot_co_so_sau_nhan_tin_hieu.png")

        self.page.locator("input[placeholder*='Tìm bot theo mã']").fill("HAH")
        self.page.wait_for_timeout(2000)
        self.screenshot("8_17_xbot__tim_kiem_hah.png")

        self.page.locator("div.gap-3 button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_21_xbot_bot_cua_toi__phai_sinh.png")

        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_22_xbot_bot_cua_toi__modal_huy_phai_sinh.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_23_xbot_bot_cua_toi__phai_sinh_sau_huy.png")

        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_24_xbot_bot_cua_toi__co_so.png")

        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("8_25_xbot_bot_cua_toi__modal_huy_co_so.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(1000)
        # self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        # self.page.wait_for_timeout(2000)
        self.screenshot("8_26_xbot_bot_cua_toi__co_so_sau_huy.png")

    @allure.feature("XBot TA")
    def capture_tab_xbot_ta_and_subtabs(self):
        self.page.locator("button:has-text('XBot TA')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_xbot_ta.png")

    @allure.feature("Bảng giá")
    def capture_tab_bang_gia_and_subtabs_full(self):
        self.page.locator("a:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_1_bang_gia_tab.png")

        self.page.locator("button:has-text('Tất cả các ngành')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_2_nganh_hien_thi_dropdown.png")

        self.page.locator("label:has-text('VN30')").click()
        self.page.locator("label:has-text('Thép')").click()
        self.screenshot("9_2_1_bo_tick_vn30_thep.png")

        self.page.mouse.click(0, 0)
        self.page.wait_for_timeout(1000)
        self.screenshot("9_3_bo_tick_vn30_thep.png")

        self.page.locator("button:has-text('Thêm mã CK')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_4_modal_them_ma_ck.png")

        self.page.locator("input[type='text']").fill("TCB")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_4_1_modal_them_ma_ck.png")

        self.page.locator("span:has-text('TCB')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_5_chon_TCB.png")

        self.page.locator("footer button:has-text('Thêm mã')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_6_sau_khi_them_ma.png")

        self.page.locator("div[tabindex='0']:has-text('TCB')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_7_modal_TCB_tong_quan.png")

        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_7_1_modal_TCB_tong_quan_1nam.png")

        self.page.locator("button:has-text('Bảng giá')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_8_modal_TCB_nhan_dinh.png")

        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_9_modal_TCB_bieu_do.png")

        self.page.locator("button:has-text('Nhận định')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_10_modal_evf_nhan_dinh.png")

        self.page.locator("button:has-text('XChart AI')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_11_xchart_ai_tab.png")

        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_1_chon_khung_thoi_gian.png")

        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_2chon_khung_thoi_gian_15.png")

        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_3_chon_khoang_thoi_gian.png")

        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_4_sau_khi_bam_nut_load.png")

        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_5_che_do_hien_thi_dropdown_mo.png")

        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_6_tuy_chinh_che_do_hien_thi_uncheck.png")

        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_7_tuy_chinh_che_do_hien_thi_check.png")

        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_11_8_chon_so_phien_du_bao.png")

        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_rrg_1d.png")

        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"9_13_1_chon_tab_{label}.png")

        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13__2Bieu_do_RRG_them_ma_ck.png")

        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_3_Bieu_do_RRG_nhap_ma_VCG.png")

        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_4_Bieu_do_RRG_chon_ma_VCG.png")

        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_13_5_Bieu_do_RRG_thêm_ma_VCG.png")

        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"9_13_6_chon_tab_{label}.png")

        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_14_dong_tien_thong_minh.png")

        self.page.locator("button:has-text('Tài chính')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_15_tai_chinh_dinh_gia.png")

        self.page.locator("button:has-text('Chỉ số tài chính')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_16_chi_so_quy_kqkd.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_1_tim_kiem_pet_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_2_tim_kiem_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_3_tim_kiem_pet_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        self.page.locator("div.flex >> text=Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_16_4_tim_kiem_pet_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(1000)
        self.screenshot("9_17_chi_so_nam_mac_dinh.png")

        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_1_tim_kiem_pet_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_2_tim_kiem_pet_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_3_tim_kiem_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_4_tim_kiem_pet_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_5_tim_kiem_pet_tai_chinh_data.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_17_6_tim_kiem_pet_chi_so_tai_chinh_data_hang_quy.png")

        self.page.locator("button:has-text('Báo cáo tài chính')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_19_bao_cao_cdkh_quy.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_20_bao_cao_cdkh_nam.png")

        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_21_kqkd_nam.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_22_kqkd_quy.png")

        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_23_luu_chuyen_quy.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_24_luu_chuyen_nam.png")

        self.page.locator("button:has-text('Hồ sơ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_25_ho_so_cong_ty.png")

        self.page.locator("button:has-text('Cổ đông & GD nội bộ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("9_26_ho_so_co_dong.png")

        self.page.locator("button[aria-label='Close']").click()

    @allure.feature("Sàn bot")
    def capture_tab_san_bot_and_subtabs(self):
        self.page.locator("a:has-text('Sàn bot')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot.png")

        self.page.locator("div.bg-card.rounded-full div.text-xs:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_nhan_tin_hieu_phai_sinh.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Tất cả')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_tat_ca.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_lenh_mo_lich_su_phai_sinh.png")

        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_phai_sinh_1.png")

        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tick_checkbox_phai_sinh.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_phai_sinh_2.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_dong_modal_phai_sinh1.png")

        self.page.locator("button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_co_so.png")

        self.page.locator("div.bg-card.rounded-full div.text-xs:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_nhan_tin_hieu_co_so.png")

        self.page.locator("div[data-slot='tabContent']:has-text('1W')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_1w_co_so.png")

        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tab_lenh_mo_lich_su_co_so.png")

        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_co_so_1.png")

        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_tick_checkbox_co_so.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_tin_hieu_co_so_2.png")

        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_dong_modal_co_so1.png")

        self.page.locator("button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_cua_toi_phai_sinh.png")

        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_huy_tin_hieu_phai_sinh.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_huy_phai_sinh.png")

        self.page.wait_for_selector("button[data-key='$.1']", state="visible", timeout=30000)
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_bot_cua_toi_co_so.png")

        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_huy_tin_hieu_co_so.png")

        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot_xac_nhan_huy_co_so.png")

    @allure.feature("Gói dịch vụ")
    def capture_tab_goi_dich_vu_and_subtabs(self):
        self.page.locator("a:has-text('Gói dịch vụ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("goi_dich_vu.png")

    @allure.feature("Lọc cổ phiếu")
    def capture_tab_loc_stock_and_subtabs(self):
        self.page.locator("a:has-text('Lọc cổ phiếu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("san_bot.png")

        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu tăng trưởng')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tang_truong_1.png")

        self.page.locator("div.relative.flex.h-10.w-full.cursor-pointer:has-text('Cổ phiếu giá trị')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri.png")

        self.page.locator("div.relative.flex.h-8.w-full.cursor-pointer:has-text('Nhóm biến động giá')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhom_bien_dong_gia.png")

        self.page.locator("div.relative.flex.h-8.w-full.cursor-pointer:has-text('Nhóm thông dụng')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhom_thong_dung.png")

        self.page.locator("div:has-text('Giá trị giao dịch trung bình 50 phiên (tỷ)')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri_gd_50_phien.png")

        self.page.locator("div:has-text('Giá trị giao dịch (tỷ)')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_gia_tri_gd.png")

        self.page.locator("div.font-semibold:has-text('BID')").first.click()
        self.page.wait_for_url("https://xno.vn/loc-co-phieu?symbol=BID&chiTietMaCK=true", timeout=20000)
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ma_bid.png")

        self.page.locator("div.gap-0 button[data-key='1nam']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ma_bid_tong_quan_1nam_ket_qua.png")

        self.page.locator("button[data-key='banggia']:has-text('Bảng giá')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bang_gia.png")

        self.page.locator("div.gap-0 button[data-key='bieudo']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bang_gia_bieu_do.png")

        self.page.locator("button[data-key='nhandinh']:has-text('Nhận định')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_nhan_dinh.png")

        self.page.locator("button:has-text('XChart AI')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_xchart_ai.png")

        self.page.locator("#resolution").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khung_thoi_gian.png")

        self.page.locator("#resolution").select_option("15")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khung_thoi_gian_15.png")

        self.page.locator("#fromDate").fill("2023-08-01")
        self.page.locator("#toDate").fill("2023-08-04")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_khoang_thoi_gian.png")

        self.page.locator("#loadButton").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_sau_khi_bam_nut_load.png")

        self.page.get_by_role("button", name="Chế độ hiển thị").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_che_do_hien_thi_dropdown_mo.png")

        self.page.locator("#showOnlyRecentPatterns").uncheck()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tuy_chinh_che_do_hien_thi_uncheck.png")

        self.page.locator("#showZigZag").check()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tuy_chinh_che_do_hien_thi_check.png")

        self.page.locator("#forecastBars").select_option("20")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chon_so_phien_du_bao.png")

        self.page.locator("button:has-text('Biểu đồ RRG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_bieu_do_rrg.png")

        tab_labels = ["10", "20", "30", "40", "50"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"loc_co_phieu_chon_tab_{label}.png")

        self.page.locator("div.flex.flex-wrap >> text=Thêm mã CK").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_them_ma_ck.png")

        self.page.locator("input[aria-label='Nhập mã CK']").fill("VCG")
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_nhap_ma_VCG.png")

        self.page.locator("span:has-text('VCG')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_chon_ma_VCG.png")

        self.page.locator("footer >> text=Thêm mã").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_Bieu_do_RRG_thêm_ma_VCG.png")

        tab_labels = ["10", "20", "30", "40"]
        for label in tab_labels:
            self.page.locator(f"div[data-slot='tabContent'] >> text={label}").click()
            self.page.wait_for_timeout(2000)
            self.screenshot(f"loc_co_phieu_chon_tab_{label}.png")

        self.page.locator("button:has-text('Dòng tiền thông minh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_dong_tien_thong_minh.png")

        self.page.locator("button[data-key='phantichtaichinh']:has-text('Tài chính')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tai_chinh.png")

        self.page.locator("button[data-key='chisotaichinh']:has-text('Chỉ số tài chính')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_hieu_qua_sinh_loi.png")

        self.page.locator("div.flex >> text=Tỷ lệ nợ xấu (NPL) & tỷ lệ bao phủ nợ xấu (LLR)").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_quy_suc_khoe_tai_chinh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam.png")

        self.page.locator("div.flex >> text=Tăng trưởng KQKD").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_tang_truong_KQKD.png")

        self.page.locator("div.flex >> text=Phân tích nguồn vốn").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_phan_tich_nguon_von.png")

        self.page.locator("div.flex >> text=Phân tích tài sản").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_pet_phan_tich_tai_san.png")

        self.page.locator("div.flex >> text=Hiệu quả sinh lời").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_hang_nam_hieu_qua_sinh_loi.png")

        self.page.locator("div.gap-0 button[data-key='data']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_tai_chinh_data.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_chi_so_tai_chinh_data_hang_quy.png")

        self.page.locator("button:has-text('Báo cáo tài chính')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu__bao_cao_tai_chinh.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_bao_cao_tai_chinh_hang_nam.png")

        self.page.locator("button:has-text('Kết quả kinh doanh')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ket_qua_kinh_doanh.png")

        self.page.locator("button:has-text('Hàng quý')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ket_qua_kinh_doanh_hang_quy.png")

        self.page.locator("button:has-text('Lưu chuyển tiền tệ')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te.png")

        self.page.locator("button:has-text('Hàng năm')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("tim_kiem_pet_luu_chuyen_tien_te_hang_nam.png")

        self.page.locator("button[data-key='thongtindoanhnghiep']:has-text('Hồ sơ')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_ho_so.png")

        self.page.locator("button[data-key='codong']:has-text('Cổ đông & GD nội bộ')").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_co_dong_gd_noi_bo.png")

        self.page.locator("button[aria-label='Close']").first.click()
        self.page.wait_for_timeout(2000)
        self.screenshot("loc_co_phieu_dong_modal.png")

    @allure.feature("Thông tin cá nhân")
    def capture_tab_thong_tin_and_subtabs(self):
        self.page.locator('button span[role="img"] svg').nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Thong_bao")

        self.page.locator('button span[role="img"] svg').nth(2).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Bat_che_do_sang")

        self.page.locator('button span[role="img"] svg').nth(1).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Thong_bao")

        self.page.locator('button span[role="img"] svg').nth(2).click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Tat_che_do_sang")

        self.page.locator("span[data-slot='trigger'][aria-haspopup='true']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan.png")

        self.page.locator("li[data-key='user-info']").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("Vao_trang_thong_tin_ca_nhan.png")

        self.page.locator("div.flex.cursor-pointer:has-text('Mật khẩu')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan_mat_khau.png")

        self.page.locator("div.flex.cursor-pointer:has-text('Gói hội viên')").click()
        self.page.wait_for_timeout(2000)
        self.screenshot("thong_tin_ca_nhan_goi_hoi_vien.png")