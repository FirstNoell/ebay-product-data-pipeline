from playwright.sync_api import sync_playwright
from scraper.ebay_extractor import extract_product


def get_products(url):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # visible for demo
        page = browser.new_page()

        print(f"🌐 Opening: {url}")
        page.goto(url, timeout=60000)

        page.wait_for_timeout(5000)

        cards = page.query_selector_all(".s-card-container")

        print(f"🔍 Found {len(cards)} cards")

        for card in cards[:20]:  # limit for demo

            data = extract_product(card)

            if data:
                results.append(data)

        browser.close()

    return results