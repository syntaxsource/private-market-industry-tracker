import sqlite3

def fetch_all_deals():
    # Connect to the existing deals database
    conn = sqlite3.connect('deals.db')
    cursor = conn.cursor()

    # Query all rows from the deals table
    cursor.execute("SELECT id, company, deal_type, amount, date, source FROM deals")
    rows = cursor.fetchall()

    conn.close()
    return rows

if __name__ == "__main__":
    deals = fetch_all_deals()

    # Display results in a simple, readable format
    for deal in deals:
        deal_id, company, deal_type, amount, date, source = deal
        print(f"[{deal_id}] {company} — {deal_type} — {amount} on {date}")
        print(f"    Source: {source}")
        print("-" * 60)
