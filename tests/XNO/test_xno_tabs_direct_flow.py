import os
import pytest
from pages.XNO.login_xno_direct import XNOLoginPageDirect
from pages.XNO.dashboard_xno_direct import XNODashboardPageDirect

@pytest.fixture(scope="function")
def login_direct_and_get_page(browser):
    context = browser.new_context()
    page = context.new_page()
    login = XNOLoginPageDirect(page)
    login.login("hnoihnoi50@gmail.com", "123456")
    yield page
    context.close()

def test_xno_full_tabs_flow(login_direct_and_get_page):
    page = login_direct_and_get_page
    os.makedirs("../../screenshots/image_xno", exist_ok=True)
    dashboard = XNODashboardPageDirect(page)

    dashboard.capture_tab_giao_dich_and_subtabs()
    dashboard.capture_tab_search_and_subtabs()
    # dashboard.capture_main_tabs()
    dashboard.capture_tab_thi_truong_and_subtabs()
    dashboard.capture_tab_co_phieu_and_subtabs()
    dashboard.capture_tab_xbot_ai_and_subtabs()
    dashboard.capture_tab_xbot_ta_and_subtabs()
    dashboard.capture_tab_bang_gia_and_subtabs_full()
    dashboard.capture_tab_san_bot_and_subtabs()
    dashboard.capture_tab_goi_dich_vu_and_subtabs()
    dashboard.capture_tab_loc_stock_and_subtabs()
    dashboard.capture_tab_thong_tin_and_subtabs()