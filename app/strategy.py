# app/strategy.py
import threading
import time
import random
from .orderbook import add_order
from . import socketio

def simulate_orders():
    while True:
        price = round(100.0 + random.uniform(-1.0, 1.0), 2)
        add_order("buy", price, 10)
        add_order("sell", price + 0.1, 10)
        socketio.emit("update", {"status": "new order"})
        time.sleep(2)

def start_strategy():
    thread = threading.Thread(target=simulate_orders, daemon=True)
    thread.start()
