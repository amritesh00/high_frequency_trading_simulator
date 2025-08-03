from flask import Blueprint, jsonify, render_template
from .redis_client import rdb
from .orderbook import Order
from .strategy import start_strategy

main_bp = Blueprint("main", __name__)

@main_bp.route("/orderbook")
def get_orderbook():
    buys = rdb.lrange("buy", 0, -1)
    sells = rdb.lrange("sell", 0, -1)

    buy_orders = [Order.from_json(o).__dict__ for o in buys]
    sell_orders = [Order.from_json(o).__dict__ for o in sells]

    return jsonify({"buy": buy_orders, "sell": sell_orders})

# ✅ Serve the frontend from /
@main_bp.route("/")
def index():
    return render_template("index.html")
