# app/__init__.py

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os
import redis
from urllib.parse import urlparse

# Load .env variables
load_dotenv()

# Set up Flask-SocketIO
socketio = SocketIO(cors_allowed_origins="*")

# Set up Redis using REDIS_URL
redis_url = urlparse(os.getenv("REDIS_URL", "redis://localhost:6379"))
rdb = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    password=redis_url.password,
    decode_responses=True
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devkey")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    socketio.init_app(app)

    from .strategy import start_strategy
    start_strategy()

    return app
