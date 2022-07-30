from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User
from app.helper_functions import create_user_safely

users_bp = Blueprint("users_bp", __name__, url_prefix="/users")

@users_bp.route("", methods=("POST",))
def create_user():
    request_body = request.get_json()
    user = create_user_safely(User, request_body)

    db.session.add(user)
    db.session.commit()
    
    return make_response(f"User {user.username} successfully created", 201)


@users_bp.route("", methods=("GET",))
def get_all_users():
    users = User.query.all()
    response_data = [user.to_dict() for user in users]
    return make_response(jsonify(response_data))