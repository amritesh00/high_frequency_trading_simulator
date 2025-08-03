# app/orderbook.py
import json
from . import rdb

ORDERBOOK_KEY = "orderbook"

def add_order(order_type, price, quantity):
    order = {"type": order_type, "price": float(price), "quantity": int(quantity)}
    rdb.rpush(ORDERBOOK_KEY, json.dumps(order))

def get_orderbook():
    data = rdb.lrange(ORDERBOOK_KEY, 0, -1)
    buy_orders = []
    sell_orders = []
    for entry in data:
        order = json.loads(entry)
        if order['type'] == 'buy':
            buy_orders.append(order)
        else:
            sell_orders.append(order)
    return {"buy": buy_orders, "sell": sell_orders}
