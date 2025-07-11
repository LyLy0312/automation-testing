# pages/login.py

from playwright.sync_api import Page

class GitHubLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username or email address")
        self.password_input = page.get_by_label("Password")
        self.signin_button = page.get_by_role("button", name="Sign in")

    def login(self, username: str, password: str) -> None:
        self.page.goto("https://github.com/login")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signin_button.click()
        
