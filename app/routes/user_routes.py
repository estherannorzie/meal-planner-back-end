from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User

users_bp = Blueprint("users_bp", __name__, url_prefix="/users")

@users_bp.route("", methods=("POST",))
def create_user():
    request_body = request.get_json()
    user = User(
        username=request_body["username"],
        first_name=request_body["first_name"],
        last_name=request_body["last_name"],
        email=request_body["email"],
    )

    db.session.add(user)
    db.session.commit()

    return make_response(f"User {user.username} successfully created", 201)