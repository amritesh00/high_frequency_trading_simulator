from .redis_client import rdb
import time

def add_order(side, price, qty):
    order_id = f"{side}:{price}:{qty}:{time.time()}"
    rdb.zadd(f"orderbook:{side}", {order_id: price})

def get_orderbook():
    book = {"buy": [], "sell": []}

    for side in ["buy", "sell"]:
        orders = rdb.zrange(f"orderbook:{side}", 0, -1, withscores=True)
        for order_id, price in orders:
            _, _, qty, _ = order_id.split(":")
            book[side].append({
                "price": price,
                "qty": int(float(qty))
            })
    return book

def match_orders():
    buy_orders = rdb.zrevrange("orderbook:buy", 0, 0, withscores=True)
    sell_orders = rdb.zrange("orderbook:sell", 0, 0, withscores=True)

    if not buy_orders or not sell_orders:
        return

    buy_id, buy_price = buy_orders[0]
    sell_id, sell_price = sell_orders[0]

    if buy_price >= sell_price:
        rdb.zrem("orderbook:buy", buy_id)
        rdb.zrem("orderbook:sell", sell_id)
