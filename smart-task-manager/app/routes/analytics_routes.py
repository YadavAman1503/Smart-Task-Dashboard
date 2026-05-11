from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.task import Task
from app.services.analytics_service import calculate_analytics

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/analytics", methods=["GET"])
@jwt_required()
def analytics():
    user_id = get_jwt_identity()

    tasks = Task.query.filter_by(user_id=user_id).all()

    analytics_data = calculate_analytics(tasks)

    return jsonify(analytics_data)