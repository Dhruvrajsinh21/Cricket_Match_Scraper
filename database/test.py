from datetime import datetime, timedelta, timezone
from db_connection import get_db
from db_queries import save_match_list
import time

def test_insert_data():
    db = get_db()

    # Define test match data to insert into the database
    matches = [
        {
            "match_id": "match_01",
            "url": "https://example.com/match1",
            "start_time": datetime.now(timezone.utc) + timedelta(minutes=1),  # Match starts in 1 minute
        },
        {
            "match_id": "match_10",
            "url": "https://example.com/match2",
            "start_time": datetime.now(timezone.utc) + timedelta(minutes=2),  # Match starts in 2 minutes
        },
    ]

    # Insert match data into the database
    print("\n=== Inserting Test Match Data ===")
    save_match_list(db, matches)
    print("Test data inserted successfully!")

    # Allow time for the real-time trigger job to process and send notifications
    print("\n=== Waiting for trigger job to process the inserted data ===")
    time.sleep(15)  # Wait for 15 seconds to allow trigger job to check the database and send notifications

    print("\n=== Test completed. Check WebSocket notifications for real-time updates! ===")

if __name__ == "__main__":
    test_insert_data()
