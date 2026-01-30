from flask import Flask, render_template
from flask_socketio import SocketIO
from app.orderbook import add_order, match, snapshot
from app.strategy import start
import os

# Create the app
app = Flask(__name__)

# Explicitly set async_mode to 'gevent'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

# Start the background HFT strategy - pass socketio so it can emit
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
    port = int(os.environ.get("PORT", 10000))
    # Use standard event loop for local dev, Gunicorn handles production
    socketio.run(app, host="0.0.0.0", port=port)    