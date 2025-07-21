import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/login.feature')

@given('the user is on the login page')
def go_to_login(page):
    page.goto("https://xno.vn/dang-nhap")

@when('the user logs in with valid credentials')
def login_with_valid(login):
    pass

@then('the user should be redirected to the dashboard')
def verify_login_success(login):
    assert login.url == "https://xno.vn/giao-dich"
