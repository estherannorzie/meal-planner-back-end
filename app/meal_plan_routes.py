from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.meal_plan import MealPlan

meal_plan_bp = Blueprint("meal_plans", __name__, url_prefix="/meal_plans")

@meal_plan_bp.route("", methods=("POST",))
def create_meal_plan():
    request_body = request.get_json()
    meal_plan = MealPlan(title=request_body["title"],
                    type=request_body["type"],
                    calories=request_body["calories"],
                    diet=request_body["diet"])

    db.session.add(meal_plan)
    db.session.commit()

    return make_response(f"Meal plan {meal_plan.title} successfully created", 201)