from playwright.sync_api import sync_playwright

def scrape_match_details(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("domcontentloaded")

            # Extract match details
            match_info = page.locator("#match-info").inner_text().strip()
            squads = page.locator("#squads").inner_text().strip()

            return {
                "match_info": match_info,
                "squads": squads,
            }

        except Exception as e:
            print(f"Error scraping match details from {url}: {e}")
            return {}

        finally:
            browser.close()
