import pytest
import allure
from pages.XNO.login_xno_direct import XNOLoginPageDirect
from playwright.sync_api import Page


@pytest.fixture(scope="class")
def login_and_get_page(browser):
    context = browser.new_context()
    page = context.new_page()
    login = XNOLoginPageDirect(page)

    with allure.step("Step 1: Đăng nhập thành công"):
        login.login("hnoihnoi50@gmail.com", "123456")

    with allure.step("Step 2: Truy cập trang thông tin cá nhân"):
        page.goto("https://xno.vn/thong-tin-ca-nhan")

    yield page
    context.close()

def reset_user_info(page: Page):
    # Reset lại thông tin ban đầu để không ảnh hưởng các test sau
    page.locator('input[name="fullname"]').fill("Nguyễn Văn A")
    page.locator('input[name="email"]').fill("hnoihnoi50@gmail.com")
    page.locator('input[name="phone"]').fill("0371112223")

@allure.epic("XNO")
@allure.feature("Thông tin cá nhân")
class TestThongTinCaNhan:

    @allure.title("TC_XNO_001 - Truy cập trang thông tin cá nhân")
    def test_truy_cap_thong_tin_ca_nhan(self, login_and_get_page: Page):
        page = login_and_get_page

        with allure.step("Kiểm tra các trường hiển thị"):
            assert page.locator('input[name="fullname"]').is_visible()
            assert page.locator('input[name="email"]').is_visible()
            assert page.locator('input[name="phone"]').is_visible()

    @allure.title("TC_XNO_002 - Cập nhật thông tin hợp lệ")
    def test_update_valid_info(self, login_and_get_page: Page):
        page = login_and_get_page

        with allure.step("Nhập thông tin hợp lệ"):
            page.locator('input[name="fullname"]').fill("Nguyễn Văn A")
            page.locator('input[name="email"]').fill("hnoihnoi50@gmail.com")
            page.locator('input[name="phone"]').fill("0371112223")

        with allure.step("Kiểm tra nút lưu được bật"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            page.wait_for_selector("button:has-text('Lưu thay đổi')", timeout=5000)
            assert save_button.get_attribute("disabled") is None
            assert "opacity-50" not in save_button.get_attribute("class")
            save_button.click()

    @allure.title("TC_XNO_003 - Để trống số điện thoại (có thông báo lỗi và nút lưu bị disable)")
    def test_empty_phone(self, login_and_get_page: Page):
        page = login_and_get_page
        page.locator('input[name="phone"]').fill("")
        page.locator('input[name="fullname"]').click()

        with allure.step("Kiểm tra thông báo lỗi hiển thị"):
            error_message = page.locator("div.text-red:has-text('Yêu cầu nhập số điện thoại')")
            page.wait_for_selector("div.text-red:has-text('Yêu cầu nhập số điện thoại')", timeout=3000)
            assert error_message.is_visible()

        with allure.step("Kiểm tra nút lưu bị mờ/disable"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.get_attribute("disabled") is not None
            assert "opacity-50" in save_button.get_attribute("class")

        with allure.step("Reset dữ liệu về ban đầu"):
            page.wait_for_timeout(3000)
            reset_user_info(page)

    @allure.title("TC_XNO_003_1 - Số điện thoại là chữ")
    def test_phone_is_text(self, login_and_get_page: Page):
        page = login_and_get_page
        page.locator('input[name="phone"]').fill("abc")
        page.locator('input[name="fullname"]').click()

        with allure.step("Kiểm tra thông báo lỗi hiển thị"):
            error_message = page.locator("div.text-red:has-text('Số điện thoại không hợp lệ')")
            page.wait_for_selector("div.text-red:has-text('Số điện thoại không hợp lệ')", timeout=3000)
            assert error_message.is_visible()

        with allure.step("Kiểm tra nút lưu bị mờ/disable"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.get_attribute("disabled") is not None
            assert "opacity-50" in save_button.get_attribute("class")

        with allure.step("Reset dữ liệu về ban đầu"):
            page.wait_for_timeout(3000)
            reset_user_info(page)

    @allure.title("TC_XNO_004 - Nhập email sai định dạng (bấm lưu nhưng email quay lại cũ)")
    def test_invalid_email(self, login_and_get_page: Page):
        page = login_and_get_page

        with allure.step("Nhập email sai định dạng"):
            page.locator('input[name="email"]').fill("abcgmail.com")
            page.locator('input[name="fullname"]').click()  # Trigger blur (nếu cần)

        with allure.step("Bấm lưu"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.is_enabled()
            save_button.click()

        with allure.step("Chờ email tự động quay lại"):
            page.wait_for_timeout(3000)
            current_email = page.locator('input[name="email"]').input_value()
            assert current_email == "hnoihnoi50@gmail.com"

    @allure.title("TC_XNO_0041 - Nhập email hợp lệ mới (bấm lưu nhưng email vẫn quay lại cũ)")
    def test_change_email_to_new_valid(self, login_and_get_page: Page):
        page = login_and_get_page

        with allure.step("Nhập email hợp lệ mới"):
            page.locator('input[name="email"]').fill("abcxyz@gmail.com")
            page.locator('input[name="fullname"]').click()  # Trigger blur

        with allure.step("Bấm lưu"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.is_enabled()
            save_button.click()

        with allure.step("Chờ email tự động quay lại"):
            page.wait_for_timeout(3000)
            current_email = page.locator('input[name="email"]').input_value()
            assert current_email == "hnoihnoi50@gmail.com"

    @allure.title("TC_XNO_005 - Nhập số điện thoại dài hơn 10 số")
    def test_invalid_phone_too_long(self, login_and_get_page: Page):
        page = login_and_get_page
        page.locator('input[name="phone"]').fill("03764937842")
        page.locator('input[name="fullname"]').click()

        with allure.step("Kiểm tra thông báo lỗi hiển thị"):
            error_message = page.locator("div.text-red:has-text('Số điện thoại không hợp lệ')")
            page.wait_for_selector("div.text-red:has-text('Số điện thoại không hợp lệ')", timeout=3000)
            assert error_message.is_visible()

        with allure.step("Kiểm tra nút lưu bị mờ/disable"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.get_attribute("disabled") is not None
            assert "opacity-50" in save_button.get_attribute("class")

        with allure.step("Reset dữ liệu về ban đầu"):
            page.wait_for_timeout(3000)
            reset_user_info(page)

    @allure.title("TC_XNO_006 - Họ và tên để trống")
    def test_fullname_empty(self, login_and_get_page: Page):
        page = login_and_get_page
        page.locator('input[name="fullname"]').fill("")
        page.locator('input[name="email"]').click()

        with allure.step("Kiểm tra thông báo lỗi hiển thị"):
            error_message = page.locator("div.text-red:has-text('Yêu cầu nhập tên')")
            page.wait_for_selector("div.text-red:has-text('Yêu cầu nhập tên')", timeout=3000)
            assert error_message.is_visible()

        with allure.step("Kiểm tra nút lưu bị mờ/disable"):
            save_button = page.locator("button:has-text('Lưu thay đổi')")
            assert save_button.get_attribute("disabled") is not None
            assert "opacity-50" in save_button.get_attribute("class")
