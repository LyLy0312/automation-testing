from playwright.sync_api import Page
from pages.Cho_tot.chotot_home import  ChototHomePage
from pages.Cho_tot.chotot_electronics import ElectronicsPage



def test_set_location_hcm(
    page: Page,
    home_page: ChototHomePage,
    electronics_page: ElectronicsPage
):
    #
    home_page.load()
    home_page.close_region_modal_if_exists()
    home_page.close_signup_banner_if_exists()
    home_page.dismiss_overlay_by_clicking()
    # Khi click vào danh mục "Đồ điện tử"
    home_page.go_to_electronics()
    page.wait_for_url("**/do-dien-tu", timeout=10000)
    # Khi click vào nút "Vị trí"
    electronics_page.open_location_picker()


    # Khi chọn "Tp Hồ Chí Minh"
    electronics_page.choose_city("Tp Hồ Chí Minh")

    # Khi nhấn "Xác nhận"
    electronics_page.confirm("Tp Hồ Chí Minh")


    # THEN: vị trí hiển thị là "Tp Hồ Chí Minh"
    assert electronics_page.selected_city() == "Tp Hồ Chí Minh"