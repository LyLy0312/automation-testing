import os
from playwright.sync_api import Page

class XNODashboardPageDirect:
    def __init__(self, page: Page):
        self.page = page

    def wait_and_capture(self, url: str, selector: str, filename: str):
        self.page.goto(url)
        self.page.wait_for_selector(selector, timeout=10000)
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", filename), full_page=True)
        print(f"[Captured] {filename}")

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

    def capture_tab_thi_truong_and_subtabs(self):
        self.page.locator("button:has-text('Thị trường')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_1_thi_truong_bien_dong__phan_bo_dong_tien.png"), full_page=True)
        print("[Captured] Biến động + Phân bổ dòng tiền")

        self.page.locator("button:has-text('Tác động đến index')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_2_thi_truong_tac_dong_index.png"), full_page=True)
        print("[Captured] Tác động đến index")

        self.page.locator("button:has-text('Nước ngoài')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_3_thi_truong_nuoc_ngoai__1nam.png"), full_page=True)
        print("[Captured] Nước ngoài - 1 năm")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_4_thi_truong_nuoc_ngoai__10phien.png"), full_page=True)
        print("[Captured] Nước ngoài - 10 phiên")

        self.page.locator("button:has-text('Tự doanh')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_5_thi_truong_tu_doanh__ytd.png"), full_page=True)
        print("[Captured] Tự doanh - YTD")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_6_thi_truong_tu_doanh__10phien.png"), full_page=True)
        print("[Captured] Tự doanh - 10 phiên")

        self.page.locator("button:has-text('Thanh khoản')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_7_thi_truong_thanh_khoan__5d.png"), full_page=True)
        print("[Captured] Thanh khoản - 5D")
        self.page.locator("button:has-text('0D')").click()
        self.page.wait_for_timeout(2000)
        self.page.screenshot(path=os.path.join("../..", "screenshots", "6_8_thi_truong_thanh_khoan__0d.png"), full_page=True)
        print("[Captured] Thanh khoản - 0D")

    def capture_tab_co_phieu_and_subtabs(self):
        def screenshot(name: str):
            self.page.wait_for_timeout(2000)
            self.page.screenshot(path=os.path.join("..", "screenshots", name), full_page=True)
            print(f"[Captured] {name}")

        self.page.locator("button:has-text('Cổ phiếu')").first.click()
        self.page.wait_for_timeout(2000)

        print("[Tab] CỔ PHIẾU > CHỈ SỐ")
        screenshot("7_1_co_phieu_chi_so__%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_2_co_phieu_chi_so__thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_3_co_phieu_chi_so__klgd.png")

        self.page.locator("div[data-slot='tabContent']:text('Cổ phiếu')").click()

        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > CỔ PHIẾU > BÙNG NỔ KL")

        screenshot("7_4_bung_no_kl__1d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_5_bung_no_kl__1d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_6_bung_no_kl__1d_gtgd.png")

        self.page.locator("button:has-text('5D')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_7_bung_no_kl__5d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_8_bung_no_kl__5d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_9_bung_no_kl__5d_gtgd.png")

        self.page.locator("div.flex >> text=Biến động giá").click()

        self.page.wait_for_timeout(2000)
        print("[Tab] CỔ PHIẾU > BIẾN ĐỘNG GIÁ")

        screenshot("7_10_bien_dong__%.png")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_11_bien_dong__thay_doi.png")

        self.page.locator("div.cursor-pointer:has-text('% 1W')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_12_bien_dong__1w.png")

        self.page.locator("div.cursor-pointer:has-text('% 1M')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_13_bien_dong__1m.png")
        self.page.locator("div.cursor-pointer:has-text('Cạn cung')").click()
        self.page.wait_for_timeout(2000)
        print("[Tab] CẠN CUNG")

        screenshot("7_15_can_cung__1d_%.png")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()

        self.page.wait_for_timeout(2000)
        screenshot("7_14_can_cung__1d_thay_doi.png")


        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_16_can_cung__1d_gtgd.png")

        self.page.locator("button:has-text('1D')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_17_can_cung__5d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_18_can_cung__5d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_19_can_cung__5d_klgd.png")

        self.page.locator("div.cursor-pointer:has-text('Vượt đỉnh')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_20_vuot_dinh__thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_21_vuot_dinh__%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)
        screenshot("7_22_vuot_dinh__gtgd.png")

        self.page.locator("div.cursor-pointer:has-text('Phá đáy')").click()

        self.page.wait_for_timeout(2000)
        screenshot("7_23_pha_day__1d_%.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(1000)
        screenshot("7_24_pha_day__1d_thay_doi.png")

        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(1000)
        screenshot("7_25_pha_day__1d_klgd.png")

        self.page.locator("button:has-text('Ngành')").click()
        self.page.wait_for_timeout(2000)
        screenshot("7_26_nganh.png")
        print("[Captured] Ngành")



