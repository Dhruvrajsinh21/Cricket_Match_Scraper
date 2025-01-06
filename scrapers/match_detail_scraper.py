import requests
from bs4 import BeautifulSoup

def scrape_match_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return {
        "match_info": soup.select_one("#match-info").text.strip(),
        "squads": soup.select_one("#squads").text.strip(),
        # "live" and "scorecard" tabs would be available after the match starts
    }
