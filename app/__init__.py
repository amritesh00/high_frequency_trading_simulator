# app/__init__.py

from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Set up Flask-SocketIO
socketio = SocketIO(cors_allowed_origins="*")

# ⛔️ Fail early if REDIS_URL is not set
redis_url_str = os.getenv("REDIS_URL")
if not redis_url_str:
    raise RuntimeError("REDIS_URL is not set in environment variables.")

# ✅ Parse the Redis URL (works with Upstash, Render secrets, etc.)

def create_app():
    # ✅ Ensure Flask uses correct template folder (root-level /templates)
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
    app = Flask(__name__, template_folder=template_dir)

    # Secret key (fallback only for local dev)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devkey")

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Initialize SocketIO
    socketio.init_app(app)

    # Start trading strategy
    from .strategy import start_strategy
    start_strategy()

    return app
