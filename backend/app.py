from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)  # <-- Flask must see this at the top level

def get_db_connection():
    conn = sqlite3.connect('deals.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/deals")
def get_deals():
    conn = get_db_connection()
    deals = conn.execute("SELECT * FROM deals").fetchall()
    conn.close()

    results = []
    for deal in deals:
        results.append({
            "id": deal["id"],
            "company": deal["company"],
            "deal_type": deal["deal_type"],
            "amount": deal["amount"],
            "date": deal["date"],
            "source": deal["source"]
        })

    return jsonify(results)

@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})

# you do NOT need app.run(...) when using `flask run`
