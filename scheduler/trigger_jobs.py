from datetime import datetime, timezone, timedelta
from database.db_connection import get_db
from database.db_queries import get_upcoming_matches, update_real_time_data
from database.db_queries import get_upcoming_matches
from scrapers.match_detail_scraper import scrape_match_details
from websock.notify import send_match_update
import asyncio

def trigger_real_time_updates():
    db = get_db()
    print("Starting real-time updates...")

    while True:
        matches = get_upcoming_matches(db)
        print(f"Retrieved {len(matches)} upcoming matches.")

        for match in matches:
            print(f"Processing match: {match['match_id']} - Start Time: {match['start_time']}")
            start_time_utc = match["start_time"].astimezone(timezone.utc) if match["start_time"].tzinfo else match["start_time"].replace(tzinfo=timezone.utc)
            current_time_utc = datetime.now(timezone.utc).replace(second=0, microsecond=0)
            start_time_utc = start_time_utc.replace(second=0, microsecond=0)
            print(f"Current UTC time: {current_time_utc}")
            print(f"Match start time (UTC): {start_time_utc}")
            tolerance_window = timedelta(minutes=5)
            if current_time_utc >= (start_time_utc - tolerance_window):
                print(f"Fetching real-time data for match: {match['match_id']}")

                # Scrape match details
                real_time_data = scrape_match_details(match["url"])
                print(f"Real-time data for match {match['match_id']}")

                # Update database
                update_real_time_data(db, match["match_id"], real_time_data)
                print(f"Updated database for match: {match['match_id']}")

                # Send WebSocket notifications
                asyncio.run(send_match_update(match["match_id"],real_time_data))
                print(f"Sent WebSocket notification for match: {match['match_id']}")
            else:
                print(f"Skipping match {match['match_id']} - Start time is in the future.")

        print("Waiting for the next update...")
        asyncio.run(asyncio.sleep(60))

