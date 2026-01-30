from .db import get_db
import time

def init_db():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            side TEXT,
            price REAL,
            quantity INTEGER,
            ts REAL
        )
    """)
    db.commit()

def add_order(side, price, qty):
    db = get_db()
    db.execute(
        "INSERT INTO orders (side, price, quantity, ts) VALUES (?, ?, ?, ?)",
        (side, price, qty, time.time())
    )
    db.commit()

def get_orderbook():
    db = get_db()
    rows = db.execute(
        "SELECT side, price, quantity FROM orders ORDER BY ts DESC LIMIT 50"
    ).fetchall()

    return [dict(row) for row in rows]

def match_orders():
    # Simple demo matching (optional)
    pass
