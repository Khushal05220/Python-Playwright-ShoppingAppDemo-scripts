from playwright.sync_api import sync_playwright

def test_order_confirmation_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.click('a[id="nav-link-accountList"]')
        page.fill('input[name="email"]', 'valid_user@example.com')
        page.click('input[id="continue"]')
        page.fill('input[name="password"]', 'valid_password')
        page.click('input[id="signInSubmit"]')

        # Simulate placing an order
        page.goto("https://www.amazon.com/cart")
        page.click('input[name="proceedToCheckout"]')

        # Verify email notification
        assert "Order Confirmation Email Sent" in page.content()

        browser.close()

if __name__ == "__main__":
    test_order_confirmation_email()
