from playwright.sync_api import sync_playwright

def test_search_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.com")
        page.fill('input[id="twotabsearchtextbox"]', 'laptop')
        page.press('input[id="twotabsearchtextbox"]', 'Enter')

        assert "laptop" in page.content()

        browser.close()

if __name__ == "__main__":
    test_search_functionality()
