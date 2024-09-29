from playwright.sync_api import sync_playwright

def test_login_with_valid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.amazon.com")
        page.click('a[id="nav-link-accountList"]')  # Clicks on Sign-In
        page.fill('input[name="email"]', 'valid_user@example.com')
        page.click('input[id="continue"]')
        page.fill('input[name="password"]', 'valid_password')
        page.click('input[id="signInSubmit"]')

        assert "Hello, User" in page.content()

        browser.close()

def test_login_with_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.amazon.com")
        page.click('a[id="nav-link-accountList"]')  # Clicks on Sign-In
        page.fill('input[name="email"]', 'invalid_user@example.com')
        page.click('input[id="continue"]')
        page.fill('input[name="password"]', 'wrong_password')
        page.click('input[id="signInSubmit"]')

        assert "There was a problem" in page.content()

        browser.close()

if __name__ == "__main__":
    test_login_with_valid_credentials()
    test_login_with_invalid_credentials()
