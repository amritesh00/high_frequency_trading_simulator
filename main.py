import eventlet
eventlet.monkey_patch()

from app import create_app, socketio
from app.strategy import run_strategy
from app.orderbook import init_db
import os

app = create_app()

init_db()
run_strategy()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
