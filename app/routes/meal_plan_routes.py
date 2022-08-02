from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.meal_plan import MealPlan

meal_plans_bp = Blueprint("meal_plans", __name__, url_prefix="/meal_plans")