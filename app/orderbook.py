orderbook = {
    "buy": [],
    "sell": []
}

def add_order(side, price, qty):
    order = {"price": price, "qty": qty}
    orderbook[side].append(order)

    orderbook["buy"] = sorted(orderbook["buy"], key=lambda x: -x["price"])
    orderbook["sell"] = sorted(orderbook["sell"], key=lambda x: x["price"])
