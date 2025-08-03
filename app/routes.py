# app/routes.py
from flask import Blueprint, jsonify, request
from .orderbook import get_orderbook, add_order
from .strategy import start_strategy
from .utils import validate_key

main_bp = Blueprint("main", __name__)


@main_bp.route("/orderbook")
def orderbook():
    return jsonify(get_orderbook())

@main_bp.route("/order", methods=["POST"])
def new_order():
    data = request.json
    if not validate_key(request.headers.get("X-API-KEY")):
        return jsonify({"error": "Invalid API key"}), 403
    add_order(data["type"], data["price"], data["quantity"])
    return jsonify({"success": True})
