def add_order(order_type, price, qty):
    from .redis_client import rdb
    rdb.rpush(order_type, f"{price}:{qty}")

def get_orderbook():
    from .redis_client import rdb
    orderbook = {"buy": [], "sell": []}
    for side in ["buy", "sell"]:
        orders = rdb.lrange(side, 0, -1)
        for entry in orders:
            price, qty = entry.split(":")
            orderbook[side].append({"price": float(price), "qty": int(qty)})
    return orderbook

def match_orders():
    from .redis_client import rdb
    buys = rdb.lrange("buy", 0, -1)
    sells = rdb.lrange("sell", 0, -1)
    matched = []
    new_buys = []
    new_sells = []

    buy_index, sell_index = 0, 0
    while buy_index < len(buys) and sell_index < len(sells):
        buy_price, buy_qty = map(float, buys[buy_index].split(":"))
        sell_price, sell_qty = map(float, sells[sell_index].split(":"))

        if buy_price >= sell_price:
            traded_qty = int(min(buy_qty, sell_qty))
            matched.append((buy_price, sell_price, traded_qty))
            buy_qty -= traded_qty
            sell_qty -= traded_qty

            if buy_qty > 0:
                new_buys.append(f"{buy_price}:{buy_qty}")
            buy_index += 1 if buy_qty <= 0 else 0

            if sell_qty > 0:
                new_sells.append(f"{sell_price}:{sell_qty}")
            sell_index += 1 if sell_qty <= 0 else 0
        else:
            new_buys.extend(buys[buy_index:])
            new_sells.extend(sells[sell_index:])
            break

    rdb.delete("buy")
    rdb.delete("sell")
    for order in new_buys:
        rdb.rpush("buy", order)
    for order in new_sells:
        rdb.rpush("sell", order)

    return matched

