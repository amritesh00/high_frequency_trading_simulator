# app/__init__.py
from flask import Flask
from flask_socketio import SocketIO
import redis
from dotenv import load_dotenv
import os

load_dotenv()

socketio = SocketIO(cors_allowed_origins="*")
rdb = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devkey")
    
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    socketio.init_app(app)
    return app
