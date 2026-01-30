import random
import time
import threading
from .orderbook import add_order, match

def auto_strategy():
    while True:
        mid = 57 + random.uniform(-2, 2)

        add_order("buy", mid - random.uniform(0, 0.5), random.randint(1, 5))
        add_order("sell", mid + random.uniform(0, 0.5), random.randint(1, 5))

        match()
        time.sleep(1)

def start():
    t = threading.Thread(target=auto_strategy, daemon=True)
    t.start()
