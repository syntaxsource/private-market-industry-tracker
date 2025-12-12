import sqlite3

# Sample data to insert into the deals table
sample_deals = [
    ("Alpha Robotics", "Series A", "$12M", "2023-10-12", "https://example.com/alpha-robotics"),
    ("Nimbus Health", "Seed Round", "$3.5M", "2023-09-01", "https://example.com/nimbus-health"),
    ("Vertex Analytics", "Acquisition", "$45M", "2023-11-05", "https://example.com/vertex-analytics"),
]

def seed_database():
    # Connect to the existing deals.db file
    conn = sqlite3.connect("deals.db")
    cursor = conn.cursor()

    # Insert all sample rows into the deals table
    cursor.executemany("""
        INSERT INTO deals (company, deal_type, amount, date, source)
        VALUES (?, ?, ?, ?, ?)
    """, sample_deals)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully.")

if __name__ == "__main__":
    seed_database()
