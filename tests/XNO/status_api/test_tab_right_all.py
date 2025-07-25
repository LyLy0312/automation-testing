import pytest
import allure
from xno_base_test import XNOBaseTest

class TestTabRightAll():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/giao-dich", "all tab right")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Thị trường")
    def test_thi_truong_and_subtabs(self):
        self.tracker.set_section("Thị trường - Biến động + Phân bổ dòng tiền")
        self.page.locator("button:has-text('Thị trường')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Tác động đến index")
        self.page.locator("button:has-text('Tác động đến index')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Nước ngoài - 1 năm")
        self.page.locator("button:has-text('Nước ngoài')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Nước ngoài - 10 phiên")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Tự doanh - YTD")
        self.page.locator("button:has-text('Tự doanh')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Tự doanh - 10 phiên")
        self.page.locator("button:has-text('10 phiên')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Thanh khoản - 5D")
        self.page.locator("button:has-text('Thanh khoản')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Thị trường - Thanh khoản - 0D")
        self.page.locator("button:has-text('0D')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()

    @allure.feature("Cổ phiếu")
    def test_co_phieu_and_subtabs(self):
        self.tracker.set_section("Cổ phiếu - Chỉ số")
        self.page.locator("button:has-text('Cổ phiếu')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Chỉ số - Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Chỉ số - KLGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL")
        self.page.locator("div[data-slot='tabContent']:has-text('Cổ phiếu')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL - 1D Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL - 1D GTGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL - 5D %")
        self.page.locator("button:has-text('5D')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL - 5D Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Bùng nổ KL - 5D GTGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Biến động giá")
        self.page.locator("div.flex >> text=Biến động giá").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Biến động giá - Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Biến động giá - 1W")
        self.page.locator("div.cursor-pointer:has-text('% 1W')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Biến động giá - 1M")
        self.page.locator("div.cursor-pointer:has-text('% 1M')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung")
        self.page.locator("div.cursor-pointer:has-text('Cạn cung')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung - 1D Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung - 1D GTGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung - 5D %")
        self.page.locator("button:has-text('1D')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung - 5D Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Cạn cung - 5D KLGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Vượt đỉnh")
        self.page.locator("div.cursor-pointer:has-text('Vượt đỉnh')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Vượt đỉnh - %")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Vượt đỉnh - GTGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Phá đáy")
        self.page.locator("div.cursor-pointer:has-text('Phá đáy')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Phá đáy - 1D Thay đổi")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(0).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Phá đáy - 1D KLGD")
        self.page.locator("div.text-end div.hover\\:text-muted.h-4.text-neutral-600").nth(1).click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Cổ phiếu - Ngành")
        self.page.locator("button:has-text('Ngành')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()

    @allure.feature("XBot AI")
    def test_xbot_ai_and_subtabs(self):
        self.tracker.set_section("XBot AI - Bot phái sinh")
        self.page.locator("button:has-text('XBot AI')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Bot cơ sở")
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Bot phái sinh - Tín hiệu")
        self.page.locator("div.gap-3 button[data-key='botphaisinh']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Bot cơ sở - Tín hiệu")
        self.page.locator("div.gap-3 button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Tìm kiếm HAH")
        self.page.locator("input[placeholder*='Tìm bot theo mã']").fill("HAH")
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Bot của tôi - Phái sinh")
        self.page.locator("div.gap-3 button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()

    @allure.feature("XBot TA")
    def test_xbot_ta_and_subtabs(self):
        self.tracker.set_section("XBot TA")
        self.page.locator("button:has-text('XBot TA')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()