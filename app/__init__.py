from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/meal_planner_development'

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.meal_plan import MealPlan
    from app.models.user import User

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes.meal_plan_routes import meal_plans_bp
    app.register_blueprint(meal_plans_bp)
    from .routes.user_routes import users_bp
    app.register_blueprint(users_bp)

    CORS(app)
    return app
