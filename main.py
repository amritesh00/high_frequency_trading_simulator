from flask import Flask, render_template, jsonify, request
from app.orderbook import get_orderbook, add_order
from app.strategy import start_strategy, stop_strategy
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orderbook")
def orderbook():
    return jsonify(get_orderbook())

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    add_order(data["side"], data["price"], data["qty"])
    return jsonify({"status": "order placed"})

@app.route("/start_strategy")
def start():
    start_strategy()
    return jsonify({"status": "Auto strategy started"})

@app.route("/stop_strategy")
def stop():
    stop_strategy()
    return jsonify({"status": "Auto strategy stopped"})

@app.route("/health")
def health():
    return jsonify({
        "status": "HFT Simulator is LIVE 🚀",
        "routes": ["/", "/orderbook", "/start_strategy", "/stop_strategy"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
