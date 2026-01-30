import time
import threading

lock = threading.Lock()
BUY = []
SELL = []

def add_order(side, price, qty):
    with lock:
        order = {
            "price": round(float(price), 2),
            "qty": int(qty),
            "time": time.time()
        }
        if side == "buy":
            BUY.append(order)
            BUY.sort(key=lambda x: (-x["price"], x["time"]))
        else:
            SELL.append(order)
            SELL.sort(key=lambda x: (x["price"], x["time"]))

def match():
    trades = []
    with lock:
        while BUY and SELL and BUY[0]["price"] >= SELL[0]["price"]:
            trade_qty = min(BUY[0]["qty"], SELL[0]["qty"])
            price = SELL[0]["price"] # Execution at the resting order's price
            
            trades.append({"price": price, "qty": trade_qty, "time": time.time()})
            
            BUY[0]["qty"] -= trade_qty
            SELL[0]["qty"] -= trade_qty

            if BUY[0]["qty"] == 0: BUY.pop(0)
            if SELL[0]["qty"] == 0: SELL.pop(0)
    return trades

def snapshot():
    with lock:
        # Return top 10 for the HFT look
        return {
            "buy": BUY[:10],
            "sell": SELL[:10]
        }