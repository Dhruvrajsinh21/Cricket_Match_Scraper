from db_connection import get_db
from db_queries import save_match_list, get_upcoming_matches, update_real_time_data
from datetime import datetime, timedelta

def test_queries():
    db = get_db()

    # Test 1: Save match list
    matches = [
        {
            "match_id": "match_001",
            "url": "https://example.com/match1",
            "start_time": datetime.utcnow() + timedelta(hours=2),
        },
        {
            "match_id": "match_002",
            "url": "https://example.com/match2",
            "start_time": datetime.utcnow() + timedelta(hours=4),
        },
    ]
    print("\n=== Testing Save Match List ===")
    save_match_list(db, matches)

    # Test 2: Get upcoming matches
    print("\n=== Testing Get Upcoming Matches ===")
    upcoming_matches = get_upcoming_matches(db)
    print("Upcoming Matches:", upcoming_matches)

    # Test 3: Update real-time data
    print("\n=== Testing Update Real-Time Data ===")
    match_id = "match_001"
    real_time_data = {"score": "100/2", "overs": "10.3"}
    update_real_time_data(db, match_id, real_time_data)

    # Verify real-time data update
    updated_match = db.matches.find_one({"match_id": match_id})
    print(f"Updated Match Data for {match_id}: {updated_match}")

if __name__ == "__main__":
    test_queries()
