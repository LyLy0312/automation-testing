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


def test_xno_all_response_status_after_click_tabs(login_direct_and_get_page):
    page = login_direct_and_get_page
    status_counts_per_tab = defaultdict(lambda: defaultdict(int))
    type_counts_per_tab = defaultdict(lambda: defaultdict(int))
    current_tab = {"name": "Giao dịch"}

    def handle_response(response):
        status = response.status
        group = (status // 100) * 100
        resource_type = response.request.resource_type or "unknown"
        tab_name = current_tab["name"]

        status_counts_per_tab[tab_name][group] += 1
        type_counts_per_tab[tab_name][resource_type] += 1

        print(f"<< {status} {response.url} (Tab: {tab_name}, Type: {resource_type})")

    page.on("response", handle_response)
    page.goto("https://xno.vn", wait_until="load")
    page.wait_for_timeout(3000)

    tabs_to_click = [
        ("Bảng giá", 5000),
        ("Lọc cổ phiếu", 5000),
        ("Gói dịch vụ", 5000),
        ("Sàn bot", 5000),
        ("Thị trường", 4000),
        ("Cổ phiếu", 4000),
        ("Xbot AI", 4000),
        ("Xbot TA", 4000),
    ]

    for tab_text, wait_time in tabs_to_click:
        print(f"\nĐang click tab: {tab_text}")
        current_tab["name"] = tab_text
        try:
            page.locator(f"text={tab_text}").click(timeout=5000)
        except:
            print(f"Không tìm thấy tab '{tab_text}'")
            continue
        page.wait_for_timeout(wait_time)

    print("\n===KẾT QUẢ THỐNG KÊ STATUS SAU KHI CLICK TABS ===")
    for tab, counts in status_counts_per_tab.items():
        print(f"\nTab: {tab}")
        for group in sorted(counts):
            prefix = "" if group == 200 else ("" if group == 400 else "" if group >= 500 else "")
            print(f"{prefix} Status {group}: {counts[group]} requests")

    print("\nTHỐNG KÊ THEO LOẠI RESOURCE TYPE ===")
    for tab, type_counts in type_counts_per_tab.items():
        print(f"\nTab: {tab}")
        for rtype, count in type_counts.items():
            print(f" {rtype}: {count} requests")
