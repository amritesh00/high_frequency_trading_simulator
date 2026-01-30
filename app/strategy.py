import threading
import random
import time
from .orderbook import add_order, match_orders

def start_auto_strategy():
    def run():
        while True:
            price = round(100 + random.uniform(-2, 2), 2)

            add_order("buy", price, random.randint(1, 5))
            add_order("sell", price + random.uniform(0.2, 0.6), random.randint(1, 5))

            match_orders()
            time.sleep(1)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
