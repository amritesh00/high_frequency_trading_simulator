quest.form["type"]
    price = float(request.form["price"])
    qty = int(request.form["qty"])
    add_order(order_type, from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from .orderbook import get_orderbook, add_order, match_orders
from .strategy import run_strategy
from app import socketio

main_bp = Blueprint("main", __name__)

@main_bp.before_app_first_request
def start_background():
    run_strategy()

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/orderbook")
def get_book():
    return jsonify(get_orderbook())

@main_bp.route("/order", methods=["POST"])
def submit_order():
    order_type = reprice, qty)
    match_orders()
    socketio.emit("orderbook_update")
    return redirect(url_for("main.index"))

