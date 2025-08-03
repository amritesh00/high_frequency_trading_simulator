# app/orderbook.py

import json
from .redis_client import rdb

class Order:
    def __init__(self, type, price, quantity):
        self.type = type
        self.price = price
        self.quantity = quantity

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Order(data["type"], data["price"], data["quantity"])

# ✅ This function allows inserting orders into Redis
def add_order(order: Order):
    key = order.type.lower()  # "buy" or "sell"
    rdb.rpush(key, order.to_json())
