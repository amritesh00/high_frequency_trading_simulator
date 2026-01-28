import threading
import time
import random
from .orderbook import add_order, match_orders
from .redis_client import rdb
from .socket import socketio

def run_strategy():
    def simulate():
        while True:
            with rdb.lock("strategy_lock", timeout=2):
                price = round(100 + random.uniform(-1, 1), 2)
                add_order("buy", price, 10)
                add_order("sell", price + 0.5, 10)
                match_orders()
                socketio.emit("orderbook_update")
            time.sleep(1)

    thread = threading.Thread(target=simulate, daemon=True)
    thread.start()
