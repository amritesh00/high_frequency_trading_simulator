import random
import time
import threading
from .orderbook import add_order, match_orders

def market_maker():
    while True:
        for _ in range(10):  # 🔥 10 auto trades/sec
            mid = round(100 + random.uniform(-1, 1), 2)

            add_order("buy", mid - random.uniform(0.1, 0.3), 10)
            add_order("sell", mid + random.uniform(0.1, 0.3), 10)

        match_orders(max_matches=3)
        time.sleep(1)

def start_strategy():
    t = threading.Thread(target=market_maker, daemon=True)
    t.start()
