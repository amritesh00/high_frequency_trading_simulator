import random
import time
import threading
from .orderbook import add_order, match_orders

def hft_strategy():
    while True:
        for _ in range(10):  # 🔥 10 transactions/sec
            base_price = round(100 + random.uniform(-1, 1), 2)

            add_order("buy", base_price, 10)
            add_order("sell", base_price + 0.5, 10)

            match_orders()

        time.sleep(1)

def start_strategy():
    t = threading.Thread(target=hft_strategy, daemon=True)
    t.start()
