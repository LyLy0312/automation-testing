import pytest
import re
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

scenarios('../features/search_stock.feature')

@given("the user is logged in")
def user_logged_in(login):
    pass

@when(parsers.parse('the user searches for "{stock_code}"'))
def search_stock(login: Page, stock_code):
    login.locator("button[aria-haspopup='dialog'] >> nth=0").click()
    login.wait_for_timeout(500)

    input_box = login.locator("input[placeholder='Tìm mã CK']")
    input_box.wait_for(state="visible", timeout=5000)
    input_box.fill(stock_code)
    login.wait_for_timeout(1000)

    item = login.locator(f"div.font-bold:has-text('{stock_code}')").first
    item.wait_for(state="visible", timeout=5000)
    item.click()
    login.wait_for_url(re.compile(rf".*symbol={stock_code}.*"), timeout=10000)

@then(parsers.parse('the stock "{stock_code}" should be in the result list'))
def verify_result(login: Page, stock_code):
    tab = login.locator(f"text={stock_code}").first
    tab.wait_for(state="visible", timeout=7000)
    assert tab.is_visible()
    print(f"Đã hiển thị mã cổ phiếu {stock_code} trên trang chi tiết.")
