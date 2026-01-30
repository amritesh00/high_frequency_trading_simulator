import random
import time
import threading
from .orderbook import add_order, match, snapshot

def auto_strategy(socketio):
    while True:
        # Simulate high frequency: 0.1s to 0.5s intervals
        price = round(100 + random.uniform(-2, 2), 2)
        
        # Randomly decide to buy or sell to create liquidity
        side = random.choice(["buy", "sell"])
        if side == "buy":
            add_order("buy", price, random.randint(1, 50))
        else:
            add_order("sell", price + 0.1, random.randint(1, 50))
        
        trades = match()
        
        # Broadcast the update to all users via WebSocket
        socketio.emit('update', {
            'book': snapshot(),
            'trades': trades
        })
        
        time.sleep(random.uniform(0.1, 0.5))

def start(socketio):
    t = threading.Thread(target=auto_strategy, args=(socketio,), daemon=True)
    t.start()