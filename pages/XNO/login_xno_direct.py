from playwright.sync_api import Page

class XNOLoginPageDirect:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        self.page.goto("https://xno.vn/dang-nhap")
        self.page.locator("input[placeholder='Vui lòng nhập email...']").fill(email)
        self.page.locator("input[placeholder='Mật khẩu đăng nhập...']").fill(password)
        self.page.locator("button[type='submit']:has-text('Đăng nhập')").click()
        self.page.wait_for_url("**/giao-dich", timeout=10000)
        print("Đăng nhập thành công")