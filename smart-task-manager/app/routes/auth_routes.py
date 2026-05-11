from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register():

    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:

        return jsonify({
            "message":"User already exists"
        })

    user = User(
        username=username,
        email=email
    )

    user.set_password(password)

    db.session.add(user)

    db.session.commit()

    return jsonify({
        "message":"Registration Successful"
    })


@auth_bp.route("/api/login", methods=["POST"])
def login():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:

        return jsonify({
            "message":"User not found"
        })

    if user.check_password(password):

        return jsonify({
            "message":"Login Successful"
        })

    return jsonify({
        "message":"Invalid Password"
    })