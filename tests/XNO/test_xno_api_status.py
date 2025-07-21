import pytest
from collections import defaultdict
from pages.XNO.login_xno_direct import XNOLoginPageDirect

@pytest.fixture(scope="function")
def login_direct_and_get_page(browser):
    context = browser.new_context()
    page = context.new_page()

    login = XNOLoginPageDirect(page)
    login.login("hnoihnoi50@gmail.com", "123456")

    yield page
    context.close()


def test_xno_status_after_login(login_direct_and_get_page):
    page = login_direct_and_get_page

    status_counts_per_page = defaultdict(lambda: defaultdict(int))

    def handle_response(response):
        if response.request.resource_type in ["xhr", "fetch"]:
            status = response.status
            group = (status // 100) * 100

            current_url = page.url
            status_counts_per_page[current_url][group] += 1
            print(f"<< {status} {response.url} (Page: {current_url})")

    page.on("response", handle_response)

    urls = [
        "https://xno.vn/giao-dich",
        "https://xno.vn/bang-gia",
        "https://xno.vn/loc-co-phieu",
        "https://xno.vn/san-bot",
        "https://xno.vn/goi-dich-vu",
        "https://xno.vn/giao-dich?rightTab=thitruong",
        "https://xno.vn/giao-dich?rightTab=cophieu",
        "https://xno.vn/giao-dich?rightTab=tinhieu",
        "https://xno.vn/giao-dich?rightTab=xbotTA",
        "https://xno.vn/thong-tin-ca-nhan"
    ]

    for url in urls:
        page.goto(url, wait_until="load")
        page.wait_for_timeout(15000)

    print("\n=== Kết quả thống kê API sau login ===")
    for url, counts in status_counts_per_page.items():
        print(f"\nTrang: {url}")
        for group in sorted(counts):
            print(f"Print {{Status API {group}: {counts[group]}; }}")
