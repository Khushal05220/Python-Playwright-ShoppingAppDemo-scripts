from playwright.sync_api import sync_playwright

def test_home_page_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        assert "Amazon" in page.title()

        # Navigate to today's deals
        page.click('a[href="/gp/goldbox"]')
        assert "Deals" in page.content()

        # Navigate to electronics category
        page.click('a[href*="/b?node=172282"]')
        assert "Electronics" in page.content()

        browser.close()

if __name__ == "__main__":
    test_home_page_navigation()
