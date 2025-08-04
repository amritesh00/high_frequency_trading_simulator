import threading
import time
import random
from .orderbook import add_order, match_orders
from .redis_client import rdb
from app import socketio

def run_strategy():
    def simulate():
        while True:
            price = 100 + random.uniform(-1, 1)
            add_order("buy", round(price, 2), 10)
            add_order("sell", round(price + 0.5, 2), 10)
            match_orders()
            socketio.emit("orderbook_update")
            time.sleep(1)
    thread = threading.Thread(target=simulate)
    thread.daemon = True
    thread.start()

