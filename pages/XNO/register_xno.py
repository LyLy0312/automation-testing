# pages/register_xno.py
from playwright.sync_api import Page
import time

class XNORegisterPage:
    def __init__(self, page: Page):
        self.page = page

    def register(self, name: str, email: str, phone: str, password: str):
        self.page.goto("https://xno.vn/dang-ky")
        self.page.wait_for_timeout(2000)

        self.page.get_by_placeholder("Vui lòng nhập họ tên...").fill(name)
        self.page.get_by_placeholder("Vui lòng nhập email...").fill(email)
        self.page.get_by_placeholder("Nhập số điện thoại...").fill(phone)

        # Phải dùng nth(0) vì có 2 ô giống placeholder
        self.page.get_by_placeholder("Mật khẩu đăng nhập...").nth(0).fill(password)

        # Xác nhận mật khẩu thì chỉ có 1
        self.page.get_by_placeholder("Xác nhận mật khẩu đăng nhập...").fill(password)

        self.page.get_by_role("button", name="Đăng ký").click()

        self.page.wait_for_timeout(3000)
        self.page.screenshot(path="register_done.png")

        self.page.get_by_text("Chúng tôi đã gửi một email xác thực", exact=False).wait_for(timeout=15000)

        print("Đăng ký xong, đợi xác minh thủ công trong Gmail...")






