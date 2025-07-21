from pages.Cho_tot.home_page import HomePage
from pages.Cho_tot.nhatot_real_estate_page import NhatotRealEstatePage
from playwright.sync_api import Page

def test_real_estate_flow(page: Page):
    home = HomePage(page)
    home.load()
    home.close_signup_banner_if_exists()
    home.dismiss_overlay_by_clicking()
    home.go_to_real_estate()
    page.wait_for_url("**nhatot.com**", timeout=10000)

    real_estate_page = NhatotRealEstatePage(page)
    real_estate_page.dismiss_overlay_if_exists()
    real_estate_page.select_house_category()
    page.wait_for_url("**/mua-ban-nha-dat", timeout=10000)

    real_estate_page.choose_city("Tp Hồ Chí Minh")

    page.wait_for_url("**/mua-ban-nha-dat-tp-ho-chi-minh", timeout=10000)
    real_estate_page.take_screenshot_of_houses_under_1_billion()
