from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history", __name__)


@history_controller.route("/history", methods=["GET"])
def list_history():
    history_records = HistoryModel.list_as_json()
    return jsonify(history_records), 200
