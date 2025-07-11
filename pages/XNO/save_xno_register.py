# save_xno_register.py

from playwright.sync_api import sync_playwright
from pages.XNO.register_xno import XNORegisterPage


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        register_page = XNORegisterPage(page)


        name = "Ly Ly"
        email = "lll336435+6@gmail.com"
        phone = "0832046745"
        password = "123456"

        register_page.register(name, email, phone, password)

        print("Đăng ký hoàn tất. Hãy vào Gmail xác minh email, rồi mới chạy login.")
        browser.close()

if __name__ == "__main__":
    run()
