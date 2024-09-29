from playwright.sync_api import sync_playwright

def test_product_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.fill('input[id="twotabsearchtextbox"]', 'iPhone')
        page.press('input[id="twotabsearchtextbox"]', 'Enter')

        # Select the first product from the search results
        page.click('span[class="celwidget slot=SEARCH_RESULTS"] a[class="a-link-normal"]')

        assert "iPhone" in page.title()

        browser.close()

if __name__ == "__main__":
    test_product_details()
