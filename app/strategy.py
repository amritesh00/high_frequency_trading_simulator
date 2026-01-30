import threading
import random
import time
from app.orderbook import add_order, orderbook

running = False

def auto_trader(socketio):
    global running
    while running:
        side = random.choice(["buy", "sell"])
        price = round(random.uniform(95, 105), 2)
        qty = random.randint(1, 10)

        add_order(side, price, qty)
        socketio.emit("orderbook_update", orderbook)

        time.sleep(2)

def start_strategy(socketio):
    global running
    if not running:
        running = True
        threading.Thread(target=auto_trader, args=(socketio,), daemon=True).start()

def stop_strategy():
    global running
    running = False
