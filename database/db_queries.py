from datetime import datetime, timezone

def save_match_list(db, matches):
    """Saves a list of matches to the database with logging."""
    if not matches:
        print("No matches to save!")
        return

    for match in matches:
        result = db.matches.update_one(
            {"match_id": match["match_id"]},
            {"$set": match},
            upsert=True
        )
        if result.upserted_id:
            print(f"Inserted new match with ID: {match['match_id']}")
        else:
            print(f"Updated match with ID: {match['match_id']}")

def get_upcoming_matches(db):
    """Fetches upcoming matches and logs the result."""
    # Ensure we compare using UTC time (timezone-aware)
    current_time_utc = datetime.now(timezone.utc)  # Get current UTC time as a timezone-aware object

    # Fetch matches where start_time is greater than or equal to the current UTC time
    matches = list(db.matches.find({"start_time": {"$gte": current_time_utc}}))
    
    if matches:
        print(f"Found {len(matches)} upcoming matches.")
    else:
        print("No upcoming matches found!")
    return matches
"""
def update_real_time_data(db, match_id, data):
    Updates real-time data for a specific match with logging
    result = db.matches.update_one(
        {"match_id": match_id},
        {"$set": {"real_time_data": data}}
    )
    if result.matched_count:
        print(f"Updated real-time data for match ID: {match_id}")
    else:
        print(f"No match found with ID: {match_id} to update!")
"""