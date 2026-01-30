orderbook = {
    "buy": [],
    "sell": []
}

def add_order(side, price, qty):
    orderbook[side].append({
        "price": round(float(price), 2),
        "qty": int(qty)
    })

def get_orderbook():
    return orderbook
