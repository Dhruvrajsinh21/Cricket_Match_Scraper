from playwright.sync_api import sync_playwright

BASE_URL = "https://crex.live/fixtures/match-list"

def scrape_match_list():
    #Scrape the match list from the specified BASE_URL and return match details.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Fetching match list...")
        page.goto(BASE_URL, timeout=60000)
        page.wait_for_load_state("domcontentloaded")

        matches = []
        try:
            match_elements = page.query_selector_all('.match-card-wrapper')
            for match in match_elements:
                try:
                    match_id = match.get_attribute("data-id")
                    url = match.get_attribute("href")
                    start_time_element = match.query_selector(".match-time")
                    start_time = start_time_element.get_attribute("data-start-time") if start_time_element else "N/A"

                    matches.append({
                        "match_id": match_id,
                        "url": url,
                        "start_time": start_time,
                    })
                except Exception as e:
                    print(f"Error parsing a match: {e}")

        except Exception as e:
            print(f"Error fetching match details: {e}")
        finally:
            browser.close()

        print(f"Successfully fetched {len(matches)} matches.")
        print(matches)
        return matches
