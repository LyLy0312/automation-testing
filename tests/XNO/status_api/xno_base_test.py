from utils.api_tracker import APIStatusTracker
from pages.XNO.login_xno_direct import XNOLoginPageDirect

class XNOBaseTest:
    def __init__(self, browser, tab_url, default_section):
        self.context = browser.new_context()
        self.page = self.context.new_page()
        self.tracker = APIStatusTracker(default_section)
        self.page.on("response", self.tracker.handle_response)

        login = XNOLoginPageDirect(self.page)
        login.login("hnoihnoi50@gmail.com", "123456")
        self.page.goto(tab_url, wait_until="load")
        self.page.wait_for_timeout(3000)

    def close(self):
        self.context.close()