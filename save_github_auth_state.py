# save_github_auth_state.py

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False để thấy trình duyệt hiện lên
        context = browser.new_context()
        page = context.new_page()

        # Truy cập vào trang login
        page.goto("https://github.com/login")

        # Điền thông tin đăng nhập
        page.get_by_label("Username or email address").fill("lili23-wq")
        page.get_by_label("Password").fill("nguyenthanhlyly@")

        # Nhấn nút đăng nhập
        page.get_by_role("button", name="Sign in").click()

        # Lưu session sau khi đăng nhập vào file state.json
        context.storage_state(path="state.json")

        browser.close()

if __name__ == "__main__":
    run()
