from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User
from app.models.meal_plan import MealPlan
from app.helper_functions import create_user_safely, get_record_by_id, create_success_message, verify_email_presence, validate_email_update_request, create_meal_plan_safely, update_user_meal_plan_safely

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=("POST",))
def create_user():
    request_body = request.get_json()
    user = create_user_safely(User, request_body)

    db.session.add(user)
    db.session.commit()
    
    return make_response(f"User {user.username} successfully created", 201)


@users_bp.route("/<user_id>", methods=("DELETE",))
def delete_user(user_id):
    user = get_record_by_id(User, user_id)

    db.session.delete(user)
    db.session.commit()
    
    return make_response(f"User {user.username} with id of {user_id} successfully deleted", 200)


@users_bp.route("", methods=("GET",))
def get_all_users():
    users = User.query.all()
    response_data = [user.to_dict() for user in users]

    return create_success_message(response_data, 200)


@users_bp.route("/<user_id>", methods=("GET",))
def get_user(user_id):
    user = get_record_by_id(User, user_id)
    return create_success_message(user.to_dict(), 200)


@users_bp.route("/<user_id>", methods=("PATCH",))
def update_user_email(user_id):
    user = get_record_by_id(User, user_id)
    request_body = request.get_json()

    validate_email_update_request(request_body)
    verify_email_presence(User, request_body["email"])

    user.update_email(request_body)
    db.session.commit()

    return create_success_message(f"User {user.username} email updated to {user.email}", 200)


@users_bp.route("/<user_id>/meal_plans", methods=("POST",))
def add_meal_plan_to_user(user_id):
    user = get_record_by_id(User, user_id)

    request_body = request.get_json()
    meal_plan = create_meal_plan_safely(MealPlan, request_body, user)

    db.session.add(meal_plan)
    db.session.commit()

    return create_success_message(f"{meal_plan.title} meal plan for user {user.username} successfully created.", 201)


@users_bp.route("/<user_id>/meal_plans", methods=("GET",))
def get_all_user_meal_plans(user_id):
    get_record_by_id(User, user_id)
    user_meal_plans = MealPlan.query.all()

    response_data = [meal_plan.to_dict() for meal_plan in user_meal_plans]

    return create_success_message(response_data, 200)


@users_bp.route("/<user_id>/meal_plans/<meal_plan_id>", methods=("DELETE",))
def delete_user_meal_plan(user_id, meal_plan_id):
    user = get_record_by_id(User, user_id)
    meal_plan = get_record_by_id(MealPlan, meal_plan_id)

    db.session.delete(meal_plan)
    db.session.commit()
    
    return make_response(f"User {user.username}'s meal plan {meal_plan.title} successfully deleted.")


@users_bp.route("/<user_id>/meal_plans/<meal_plan_id>", methods=("PUT",))
def update_user_meal_plan(user_id, meal_plan_id):
    user = get_record_by_id(User, user_id)
    meal_plan = get_record_by_id(MealPlan, meal_plan_id)

    request_body = request.get_json()
    update_user_meal_plan_safely(MealPlan, request_body, meal_plan)
    
    db.session.commit()
    
    return make_response(f"User {user.username}'s meal plan updated to {meal_plan.title} successfully.")