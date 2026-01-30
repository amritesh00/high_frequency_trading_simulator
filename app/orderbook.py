import time

BUY_ORDERS = []
SELL_ORDERS = []

def add_order(side, price, qty):
    order = {
        "side": side,
        "price": price,
        "qty": qty,
        "time": time.time()
    }

    if side == "buy":
        BUY_ORDERS.append(order)
        BUY_ORDERS.sort(key=lambda x: (-x["price"], x["time"]))
    else:
        SELL_ORDERS.append(order)
        SELL_ORDERS.sort(key=lambda x: (x["price"], x["time"]))

def match_orders():
    while BUY_ORDERS and SELL_ORDERS:
        buy = BUY_ORDERS[0]
        sell = SELL_ORDERS[0]

        if buy["price"] >= sell["price"]:
            qty = min(buy["qty"], sell["qty"])
            buy["qty"] -= qty
            sell["qty"] -= qty

            if buy["qty"] == 0:
                BUY_ORDERS.pop(0)
            if sell["qty"] == 0:
                SELL_ORDERS.pop(0)
        else:
            break

def get_orderbook():
    return {
        "buy": BUY_ORDERS[:10],
        "sell": SELL_ORDERS[:10]
    }
