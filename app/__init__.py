# app/__init__.py

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    from .strategy import run_strategy
    run_strategy()  # ✅ Start background strategy thread here

    socketio.init_app(app)
    return app
