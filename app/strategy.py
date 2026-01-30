import random
import time
import threading
from .orderbook import add_order, match

def auto_strategy():
    while True:
        # 1. Generate a price centered around 100 with small noise
        price = round(100 + random.uniform(-1, 1), 2)
        
        # 2. Add the Buy Order (Bid) at the generated price
        add_order("buy", price, 10)
        
        # 3. Add the Sell Order (Ask) at a 0.50 markup
        add_order("sell", price + 0.5, 10)
        
        # 4. Attempt to match orders and wait
        match()
        # Note: If you need to emit to SocketIO here, 
        # ensure 'socketio' is imported or passed in.
        
        time.sleep(1)

def start():
    t = threading.Thread(target=auto_strategy, daemon=True)
    t.start()