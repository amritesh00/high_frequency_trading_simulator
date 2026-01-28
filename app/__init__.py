from flask import Flask
from dotenv import load_dotenv
import os
from .socket import socketio

def create_app():
    load_dotenv()

    app = Flask(__name__, template_folder="../templates")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    socketio.init_app(app)
    return app
