import pytest
import allure
from xno_base_test import XNOBaseTest

class TestTabSanBot:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base = XNOBaseTest(browser, "https://xno.vn/san-bot", "Sàn bot")
        self.page = self.base.page
        self.tracker = self.base.tracker
        yield
        self.base.close()

    @allure.feature("Sàn bot")
    def test_san_bot_click_subtabs(self):
        self.tracker.set_section("Nhận tín hiệu - Bot phái sinh")
        self.page.locator("div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn tab Tất cả - Bot phái sinh")
        self.page.locator("div[data-slot='tabContent']:has-text('Tất cả')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn tab Lệnh mở - Lịch sử - Bot phái sinh")
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận nhận tín hiệu - Bot phái sinh")
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tick checkbox - Bot phái sinh")
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận nhận tín hiệu - Bot phái sinh")
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Đóng modal và thông báo - Bot phái sinh")
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chuyển sang Bot cơ sở")
        self.page.locator("button[data-key='botcoso']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Nhận tín hiệu - Bot cơ sở")
        self.page.locator("div.rounded-full:has-text('Nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn tab 1W - Bot cơ sở")
        self.page.locator("div[data-slot='tabContent']:has-text('1W')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chọn tab Lệnh mở - Lịch sử - Bot cơ sở")
        self.page.locator("div[data-slot='tabContent']:has-text('Lệnh mở - Lịch sử')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận nhận tín hiệu - Bot cơ sở")
        self.page.locator("section[role='dialog'] div.text-refine-bg:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Tick checkbox - Bot cơ sở")
        self.page.locator("section[role='dialog'] div.gap-1 input[type='checkbox']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận nhận tín hiệu - Bot cơ sở")
        self.page.locator("section[role='dialog'] footer button:has-text('Nhận tín hiệu')").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Đóng modal và thông báo - Bot cơ sở")
        self.page.locator("button[aria-label='Close']").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("XBot AI - Bot của tôi - Phái sinh")
        self.page.locator("button[data-key='botcuatoi']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Hủy nhận tín hiệu - Bot của tôi - Phái sinh")
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận hủy - Bot của tôi - Phái sinh")
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Chuyển sang Bot của tôi - Cơ sở")
        self.page.wait_for_selector("button[data-key='$.1']", state="visible", timeout=30000)
        self.page.locator("button[data-key='$.1']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Hủy nhận tín hiệu - Bot của tôi - Cơ sở")
        self.page.locator("div.rounded-full:has-text('Hủy nhận tín hiệu')").first.click()
        self.page.wait_for_timeout(2000)

        self.tracker.set_section("Xác nhận hủy - Bot của tôi - Cơ sở")
        self.page.locator("section[role='dialog'] footer button:has-text('Xác nhận hủy')").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("div.Toastify__toast--success button[aria-label='close']").click()
        self.page.wait_for_timeout(2000)

        self.tracker.print_summary()

    @allure.feature("Gói dịch vụ")
    def test_xbot_ta_and_subtabs(self):
        self.tracker.set_section("Gói dịch vụ")
        self.page.locator("a:has-text('Gói dịch vụ')").click()
        self.page.wait_for_timeout(3000)

        self.tracker.print_summary()