from playwright.sync_api import sync_playwright

def test_order_history():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.click('a[id="nav-link-accountList"]')
        page.fill('input[name="email"]', 'valid_user@example.com')
        page.click('input[id="continue"]')
        page.fill('input[name="password"]', 'valid_password')
        page.click('input[id="signInSubmit"]')

        # Go to Order History
        page.click('a[href*="/gp/your-account/order-history"]')

        assert "Your Orders" in page.content()

        browser.close()

if __name__ == "__main__":
    test_order_history()
