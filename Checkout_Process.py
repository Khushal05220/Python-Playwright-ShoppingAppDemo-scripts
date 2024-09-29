from playwright.sync_api import sync_playwright

def test_checkout_process():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.fill('input[id="twotabsearchtextbox"]', 'book')
        page.press('input[id="twotabsearchtextbox"]', 'Enter')

        # Select the first product from the search results
        page.click('span[class="celwidget slot=SEARCH_RESULTS"] a[class="a-link-normal"]')
        page.click('input[id="add-to-cart-button"]')

        # Proceed to checkout
        page.click('a[id="hlb-ptc-btn-native"]')

        assert "Sign-In" in page.content()

        browser.close()

if __name__ == "__main__":
    test_checkout_process()
