from apscheduler.schedulers.background import BackgroundScheduler
from scrapers.match_list_scraper import scrape_match_list
from database.db_connection import get_db
from database.db_queries import save_match_list

def update_match_list():
    db = get_db()
    matches = scrape_match_list()
    save_match_list(db, matches)

def run_scheduler():
    scheduler = BackgroundScheduler()
    try:
        scheduler.add_job(update_match_list, "interval", seconds=30)
        print("Scheduler started. Press Ctrl+C to exit.")
        scheduler.start()
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        print("Shutting down scheduler...")
    finally:
        scheduler.shutdown()
