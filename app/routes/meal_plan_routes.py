from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.meal_plan import MealPlan
from app.helper_functions import get_record_by_id, create_meal_plan_safely

meal_plans_bp = Blueprint("meal_plans", __name__, url_prefix="/meal_plans")

@meal_plans_bp.route("/<user_id>/meal_plans", methods=("POST",))
def add_meal_plan_to_user(user_id):
    user = get_record_by_id(MealPlan, user_id)

    request_body = request.get_json()
    meal_plan = create_meal_plan_safely(MealPlan, request_body)

    db.session.commit(meal_plan)

    return make_response(f"{meal_plan.title} meal plan for user {user.username} successfully created.", 201)