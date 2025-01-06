import requests
from bs4 import BeautifulSoup

BASE_URL = "https://crex.live/fixtures/match-list"

def scrape_match_list():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Successfully fetched the page!")
    else:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return []

    # Check the raw HTML content
    print(response.text[:1000])  # Print only the first 1000 characters for inspection

    soup = BeautifulSoup(response.content, "html.parser")

    matches = []
    for match in soup.select(".match-list-item"):
        try:
            match_id = match["data-id"]
            url = match.select_one(".match-link")["href"]
            start_time = match.select_one(".match-time")["data-start-time"]
            matches.append({
                "match_id": match_id,
                "url": url,
                "start_time": start_time,
            })
        except Exception as e:
            print(f"Error parsing a match: {e}")

    print(matches)
    return matches
