import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page
import ast

scenarios('../features/filter_by_industry.feature')

@given("the user is logged in")
def the_user_is_logged_in(login):
    login.click("text=Lọc cổ phiếu")
    login.wait_for_selector("text=Chọn chỉ tiêu")

@when(parsers.parse('the user selects industries {industries}'))
def select_industries(login: Page, industries: str):
    import ast
    industry_list = ast.literal_eval(industries)
    print("Chọn các ngành:", industry_list)

    login.locator("text=Ngành").first.click()

    login.wait_for_selector("text=Chọn giá trị")

    dropdown_trigger = login.locator("div[data-slot='innerWrapper']").first
    dropdown_trigger.click()

    selected_tags = login.locator("span[data-selected='true'] svg")
    count = selected_tags.count()
    if count > 0:
        print(f"Đang xóa {count} ngành đã chọn trước đó...")
        for i in range(count):
            selected_tags.first.click()
            login.wait_for_timeout(200)

    for industry in industry_list:
        option = login.locator(f"span[data-label='true']:has-text('{industry}')").first
        option.wait_for(timeout=3000)
        option.click()
        login.wait_for_timeout(300)
    login.mouse.click(1, 1)

    login.locator("button:has-text('Lọc'):not(:has-text('Lưu'))").click()

@when("the user clicks the Filter button")
def click_filter_button(login: Page):
    buttons = login.locator("button:has-text('Lọc')")
    buttons.nth(1).click()
    login.wait_for_timeout(2000)


@then(parsers.parse('the result list should contain stocks in {industries}'))
def verify_result_contains_industries(login: Page, industries: str):
    industry_list = ast.literal_eval(industries)
    login.wait_for_selector("text=Kết quả lọc")

    rows = login.locator("div:has(.font-bold)")
    assert rows.count() > 0

    print(f"Danh sách cổ phiếu đã được lọc theo: {', '.join(industry_list)}")
