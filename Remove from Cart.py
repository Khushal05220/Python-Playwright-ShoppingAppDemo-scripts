from playwright.sync_api import sync_playwright

def test_remove_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.fill('input[id="twotabsearchtextbox"]', 'headphones')
        page.press('input[id="twotabsearchtextbox"]', 'Enter')

        # Select the first product from the search results
        page.click('span[class="celwidget slot=SEARCH_RESULTS"] a[class="a-link-normal"]')
        page.click('input[id="add-to-cart-button"]')

        # Go to cart and remove the product
        page.click('a[id="nav-cart"]')
        page.click('input[value="Delete"]')

        assert "was removed from Shopping Cart" in page.content()

        browser.close()

if __name__ == "__main__":
    test_remove_from_cart()
