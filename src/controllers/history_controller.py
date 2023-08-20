from flask import Blueprint, jsonify
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/history/", methods=["GET"])
def get_history():
    history = HistoryModel.list_as_json()

    return jsonify(history), 200
