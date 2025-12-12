import sqlite3               
import logging               # Enables structured logging for debugging and monitoring.
from pathlib import Path     # Provides clean, cross-platform filesystem paths.

# Configure logging: write INFO+ messages to app.log with timestamps.
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s" 
)

# Path object representing the database file.
DB_PATH = Path("deals.db")

def fetch_all_deals():
    # If the database file doesn't exist, log an error and return nothing.
    if not DB_PATH.exists():
        logging.error(f"Database file not found: {DB_PATH.resolve()}")
        return []

    try:
        # Safely open a connection using context manager (auto-closes).
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Query all deals, ordered by date (newest first).
            cursor.execute("""
                SELECT id, company, deal_type, amount, date, source
                FROM deals
                ORDER BY date DESC
            """)
            rows = cursor.fetchall()

            logging.info(f"Retrieved {len(rows)} deals")
            return rows

    except sqlite3.Error as e:
        # Log any database-related errors.
        logging.error(f"SQLite error: {e}")
        return []

def display_deals(deals):
    # If there are no deals, print a simple message.
    if not deals:
        print("No deals found.")
        return

    # Nicely format each deal in the terminal.
    for deal in deals:
        deal_id, company, deal_type, amount, date, source = deal
        print(f"[{deal_id}] {company} — {deal_type} — {amount} on {date}")
        print(f"    Source: {source}")
        print("-" * 60)

# Script entry point.
if __name__ == "__main__":
    logging.info("Starting safe deal viewer...")
    deals = fetch_all_deals()
    display_deals(deals)
    logging.info("Completed deal viewer run.")
