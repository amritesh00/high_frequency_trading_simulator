# ==============================
# main.py
# HFT Simulator – Render Ready
# ==============================

import eventlet
eventlet.monkey_patch()

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import os
import threading
import time
import random

# ------------------------------
# App & Socket Setup
# ------------------------------
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="eventlet"
)

# ------------------------------
# In-memory Orderbook (Demo)
# ------------------------------
orderbook = {
    "buy": [],
    "sell": []
}

strategy_running = False


# ------------------------------
# Routes
# ------------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "HFT Simulator is LIVE 🚀",
        "message": "Backend running successfully on Render",
        "routes": [
            "/orderbook",
            "/order (POST)",
            "/start_strategy",
            "/stop_strategy"
        ]
    })


@app.route("/orderbook")
def get_orderbook():
    return jsonify(orderbook)


@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    side = data.get("side")
    price = float(data.get("price"))
    qty = int(data.get("qty"))

    if side not in ["buy", "sell"]:
        return jsonify({"error": "Invalid side"}), 400

    order = {
        "price": price,
        "qty": qty,
        "timestamp": time.time()
    }

    orderbook[side].append(order)

    socketio.emit("orderbook_update", orderbook)

    return jsonify({"status": "Order placed"}), 200


@app.route("/start_strategy")
def start_strategy():
    global strategy_running
    if not strategy_running:
        strategy_running = True
        threading.Thread(target=auto_strategy, daemon=True).start()
    return jsonify({"status": "Auto strategy started"})


@app.route("/stop_strategy")
def stop_strategy():
    global strategy_running
    strategy_running = False
    return jsonify({"status": "Auto strategy stopped"})


# ------------------------------
# Auto Trading Strategy (Demo)
# ------------------------------
def auto_strategy():
    global strategy_running

    while strategy_running:
        side = random.choice(["buy", "sell"])
        price = round(random.uniform(90, 110), 2)
        qty = random.randint(1, 10)

        orderbook[side].append({
            "price": price,
            "qty": qty,
            "timestamp": time.time()
        })

        socketio.emit("orderbook_update", orderbook)
        time.sleep(2)


# ------------------------------
# Socket.IO Events
# ------------------------------
@socketio.on("connect")
def handle_connect():
    emit("orderbook_update", orderbook)


# ------------------------------
# Run on Render
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    socketio.run(app, host="0.0.0.0", port=port)
