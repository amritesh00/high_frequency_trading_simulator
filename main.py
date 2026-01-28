import os

from app import create_app
from app.socket import socketio
from app.strategy import run_strategy

app = create_app()
run_strategy()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
