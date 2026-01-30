import threading
import time
import random
from .orderbook import add_order

def run_strategy():
    def simulate():
        while True:
            price = round(100 + random.uniform(-1, 1), 2)
            add_order("buy", price, 10)
            add_order("sell", price + 0.5, 10)
            time.sleep(1)

    t = threading.Thread(target=simulate, daemon=True)
    t.start()
