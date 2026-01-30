from flask import Flask, render_template, jsonify, request
from app.orderbook import add_order, match_orders, get_orderbook
from app.strategy import start_auto_strategy
import os

app = Flask(__name__)

# 🔥 Start strategy automatically
start_auto_strategy()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/orderbook")
def orderbook():
    return jsonify(get_orderbook())

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    add_order(data["side"], float(data["price"]), int(data["qty"]))
    match_orders()
    return {"status": "order placed"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
