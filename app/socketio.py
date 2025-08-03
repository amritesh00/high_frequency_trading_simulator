# app/socketio.py
from flask_socketio import SocketIO
from flask import Flask
import eventlet

# Make sure monkey patching is applied before anything else
eventlet.monkey_patch()

socketio = SocketIO(async_mode="eventlet", cors_allowed_origins="*")
