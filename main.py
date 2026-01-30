from flask import Flask, render_template
from flask_socketio import SocketIO
from app.orderbook import add_order, match, snapshot
from app.strategy import start
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Start the background HFT strategy
start(socketio)

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on('manual_order')
def handle_manual_order(data):
    add_order(data["side"], data["price"], data["qty"])
    trades = match()
    socketio.emit('update', {
        'book': snapshot(),
        'trades': trades
    })

if __name__ == "__main__":
    # For Render, we use eventlet to handle the WebSocket connections
    port = int(os.environ.get("PORT", 10000))
    socketio.run(app, host="0.0.0.0", port=port, log_output=True)