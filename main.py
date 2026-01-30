import eventlet
eventlet.monkey_patch()

from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO
from app.orderbook import orderbook, add_order
from app.strategy import start_strategy, stop_strategy

app = Flask(__name__)
app.config["SECRET_KEY"] = "hft-secret"

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return jsonify({
        "status": "HFT Simulator is LIVE 🚀",
        "message": "Backend running successfully on Render",
        "routes": ["/orderbook", "/order (POST)", "/start_strategy", "/stop_strategy"]
    })

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/orderbook")
def get_orderbook():
    return jsonify(orderbook)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    add_order(data["side"], data["price"], data["qty"])
    socketio.emit("orderbook_update", orderbook)
    return jsonify({"status": "order placed"})

@app.route("/start_strategy")
def start():
    start_strategy(socketio)
    return jsonify({"status": "Auto strategy started"})

@app.route("/stop_strategy")
def stop():
    stop_strategy()
    return jsonify({"status": "Auto strategy stopped"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
