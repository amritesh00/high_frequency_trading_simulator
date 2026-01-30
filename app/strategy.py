import threading
import time
import random
from .orderbook import add_order

running = False
thread = None

def strategy_loop():
    global running
    while running:
        price = 100 + random.uniform(-1, 1)
        add_order("buy", price, 10)
        add_order("sell", price + 0.5, 10)
        time.sleep(1)

def start_strategy():
    global running, thread
    if running:
        return
    running = True
    thread = threading.Thread(target=strategy_loop)
    thread.daemon = True
    thread.start()

def stop_strategy():
    global running
    running = False
