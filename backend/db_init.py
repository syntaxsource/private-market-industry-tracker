import sqlite3   # SQLite library for creating and interacting with a lightweight database file

# Connect to (or create) the database file.
# If 'deals.db' does not exist in the same folder, SQLite will automatically create it.
conn = sqlite3.connect('deals.db')

# Create a cursor object that allows us to execute SQL commands.
cursor = conn.cursor()

# Create the 'deals' table if it doesn't already exist.
# This table will store all scraped deal information with clearly defined columns.
cursor.execute('''
CREATE TABLE IF NOT EXISTS deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each deal (auto-generated)
    company TEXT,                          -- Name of the company involved in the deal
    deal_type TEXT,                        -- Category/type of deal (e.g., acquisition, funding round)
    amount TEXT,                           -- Deal amount (stored as text to support various formats)
    date TEXT,                             -- Date of the deal
    source TEXT                            -- URL or publication source of the information
)
''')

# Save (commit) any changes made to the database structure.
conn.commit()

# Close the connection to free system resources.
conn.close()

# Confirmation message so you know the script completed successfully.
print("Database initialized and deals table created.")

