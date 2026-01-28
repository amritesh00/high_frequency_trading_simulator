from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from .orderbook import add_order, get_orderbook, match_orders
from .socket import socketio

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/orderbook")
def orderbook():
    return jsonify(get_orderbook())

@main_bp.route("/order", methods=["POST"])
def submit_order():
    side = request.form["type"]
    price = float(request.form["price"])
    qty = int(request.form["qty"])

    add_order(side, price, qty)
    match_orders()
    socketio.emit("orderbook_update")

    return redirect(url_for("main.index"))
