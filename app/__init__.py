# app/__init__.py

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    load_dotenv()
    app = Flask(__name__, template_folder="../templates")  # if templates is outside /app
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")
    # if templates is outside /app


    from .routes import main_bp
    app.register_blueprint(main_bp)

    from .strategy import run_strategy
    run_strategy()  # ✅ Start background strategy thread here

    socketio.init_app(app)
    return app
