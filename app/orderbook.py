import time
import threading

lock = threading.Lock()

BUY = []
SELL = []
TRADES = []

def add_order(side, price, qty):
    with lock:
        order = {
            "price": round(price, 2),
            "qty": qty,
            "time": time.time()
        }
        if side == "buy":
            BUY.append(order)
            BUY.sort(key=lambda x: (-x["price"], x["time"]))
        else:
            SELL.append(order)
            SELL.sort(key=lambda x: (x["price"], x["time"]))

def match_orders():
    with lock:
        while BUY and SELL and BUY[0]["price"] >= SELL[0]["price"]:
            trade_qty = min(BUY[0]["qty"], SELL[0]["qty"])
            trade_price = SELL[0]["price"]

            BUY[0]["qty"] -= trade_qty
            SELL[0]["qty"] -= trade_qty

            TRADES.append({
                "price": trade_price,
                "qty": trade_qty,
                "time": time.time()
            })

            if BUY[0]["qty"] == 0:
                BUY.pop(0)
            if SELL[0]["qty"] == 0:
                SELL.pop(0)

            if len(TRADES) > 20:
                TRADES.pop(0)

def snapshot():
    with lock:
        return {
            "buy": BUY[:10],
            "sell": SELL[:10],
            "trades": TRADES[:]
        }
