from flask import Flask, render_template, jsonify, request
from app.orderbook import add_order, match_orders, snapshot
from app.strategy import start_strategy
import os

app = Flask(__name__)

# 🚀 Auto-start strategy
start_strategy()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orderbook")
def orderbook():
    return jsonify(snapshot())

@app.route("/order", methods=["POST"])
def manual_order():
    data = request.json
    add_order(data["side"], float(data["price"]), int(data["qty"]))
    match_orders(max_matches=5)
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
