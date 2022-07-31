from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.meal_plan import MealPlan
from app.helper_functions import get_record_by_id, create_meal_plan_safely

meal_plan_bp = Blueprint("meal_plan_bp", __name__, url_prefix="/<user_id>/meal_plans")

@meal_plan_bp.route("", methods=("POST",))
def create_meal_plan(user_id):
    user = get_record_by_id(MealPlan, user_id)
    request_body = request.get_json()
    meal_plan = create_meal_plan_safely(MealPlan, request_body)

    db.session.add(meal_plan)
    db.session.commit()

    return make_response(f"{meal_plan.title} meal plan for user {} successfully created.", 201)