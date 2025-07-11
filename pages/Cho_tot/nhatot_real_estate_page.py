from playwright.sync_api import Page, expect

class NhatotRealEstatePage:
    def __init__(self, page: Page):
        self.page = page

    def dismiss_overlay_if_exists(self):
        overlay = self.page.locator("div.aw__s1tlv3pf")

        try:
            overlay.wait_for(state="visible", timeout=5000)
            print("Overlay xuất hiện, click để ẩn đi...")
            self.page.mouse.click(10, 10)
            overlay.wait_for(state="hidden", timeout=10000)
            print("Overlay đã được ẩn.")
        except:
            print("Overlay không xuất hiện, bỏ qua.")

    def select_house_category(self):
        print("Đang hover vào mục 'Mua bán'...")

        self.page.wait_for_selector("h2.hki46p2", timeout=10000)

        mua_ban = self.page.locator("img[alt='Mua bán']").first
        expect(mua_ban).to_be_visible(timeout=10000)
        mua_ban.hover()
        print("Đã hover vào mục 'Mua bán'.")

        self.page.wait_for_selector("a[href='mua-ban-nha-dat']", timeout=10000)

        house_link = self.page.locator("a[href='mua-ban-nha-dat']")
        expect(house_link).to_be_visible(timeout=10000)
        house_link.click()
        print("Đã click vào mục 'Nhà ở'.")

    def choose_city(self, city: str):
        print(f"Đang chọn thành phố: {city}...")

        # Tạo selector tìm thẻ <a> chứa tên thành phố (case-insensitive)
        city_selector = f"a.l1odfxq:has-text('{city}')"
        city_link = self.page.locator(city_selector).first

        expect(city_link).to_be_visible(timeout=10000)
        city_link.scroll_into_view_if_needed()
        city_link.click()

        print(f"Đã chọn thành phố: {city}")

    def take_screenshot_of_houses_under_1_billion(self):
        print("Đang tìm các nhà dưới 1 tỷ...")
        self.page.wait_for_timeout(3000)  # Chờ load

        prices = self.page.locator("span.bfe6oav")

        count = prices.count()
        print(f"Tổng số element giá: {count}")

        for i in range(count):
            price_text = prices.nth(i).inner_text().strip()

            if not ('triệu' in price_text or 'tỷ' in price_text):
                continue

            price_vnd = self._parse_price(price_text)

            if price_vnd is not None and price_vnd < 1_000_000_000:
                print(f"Nhà có giá {price_text} ({price_vnd:,} VND) < 1 tỷ. Chụp hình...")

                listing_element = prices.nth(i).locator("xpath=ancestor::li[@itemtype='http://schema.org/ListItem']")
                listing_element.scroll_into_view_if_needed()
                listing_element.screenshot(path=f"../screenshots/house_under_1_billion_{i}.png")
            else:
                print(f"Giá {price_text} >= 1 tỷ hoặc không hợp lệ.")

    def _parse_price(self, price_text: str) -> int:
        try:
            price_text = price_text.lower().replace(",", "").replace(" ", "")
            if "tỷ" in price_text:
                value = float(price_text.replace("tỷ", ""))
                return int(value * 1_000_000_000)
            elif "triệu" in price_text:
                value = float(price_text.replace("triệu", ""))
                return int(value * 1_000_000)
            return None
        except:
            return None



