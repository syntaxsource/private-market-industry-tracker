import requests                     # HTTP client for fetching website data
from bs4 import BeautifulSoup        # HTML parser used to extract structured elements from the page
import sqlite3                       # SQLite library for inserting scraped deals into deals.db


def scrape_demo_page():
    # Target URL for demonstration. In a live workflow, this would be replaced
    # with real news, funding, or M&A pages from industry sources.
    url = "https://example.com/sample-deals"

    # Send an HTTP GET request and retrieve the full HTML content.
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup to make it searchable.
    soup = BeautifulSoup(response.text, "html.parser")

    # Container for all extracted deal tuples.
    deals = []

    # Loop over each deal “card” on the page, identified by its CSS class.
    for item in soup.select(".deal-item"):
        # Extract individual fields using CSS selectors.
        company = item.select_one(".company").get_text(strip=True)
        deal_type = item.select_one(".type").get_text(strip=True)
        amount = item.select_one(".amount").get_text(strip=True)
        date = item.select_one(".date").get_text(strip=True)

        # Save the source URL so downstream processes know where the deal originated.
        source = url

        # Append a tuple in the exact order expected by the database schema.
        deals.append((company, deal_type, amount, date, source))

    # Return a list of extracted deal tuples.
    return deals


def save_deals_to_db(deals):
    # Open a connection to the SQLite database.
    conn = sqlite3.connect("deals.db")
    cursor = conn.cursor()

    # Insert all scraped deals in bulk using executemany for efficiency.
    cursor.executemany("""
        INSERT INTO deals (company, deal_type, amount, date, source)
        VALUES (?, ?, ?, ?, ?)
    """, deals)

    # Commit write operations and close the connection.
    conn.commit()
    conn.close()

    # Basic confirmation feedback for testing.
    print(f"{len(deals)} new deals inserted.")


# Script entry point: scrape the demo page and insert results into the database.
if __name__ == "__main__":
    scraped_deals = scrape_demo_page()
    save_deals_to_db(scraped_deals)
