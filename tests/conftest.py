import pytest
from app import create_app
from app import db
from app.models.user import User
from app.models.meal_plan import MealPlan
import datetime
from flask.signals import request_finished


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def saved_users(app):
    user_1 = User(
        username="eggpioneer10", 
        first_name="Vance", 
        last_name="Lehner", 
        email="Vance.Lehner90@gmail.com"
    )

    user_2 = User(
        username="fishalienpie", 
        first_name="Lora", 
        last_name="Kassulke", 
        email="Lora.Kassulke75@yahoo.com"
    )

    user_3 = User(
        username="nailspotato", 
        first_name="Katelin", 
        last_name="Gulgowski", 
        email="Katelin_Gulgowski94@hotmail.com"
    )

    db.session.add_all([user_1, user_2, user_3])
    db.session.commit()
    users = {
        "user_1": user_1, 
        "user_2": user_2, 
        "user_3": user_3
    }
    return users


@pytest.fixture
def saved_users_meal_plans(app, saved_users):
    meal_plan_for_user_1 = MealPlan(
        title="Oscar Mayer Extra Cheesy Pizza Lunchables",
        type=4,
        calories=280,
        date=datetime.date.today(),
        user=saved_users["user_1"]
    )

    meal_plan_for_user_2 = MealPlan(
        title="Spaghetti & Meatballs with Tomato Sauce, small",
        type=3,
        calories=412,
        date=datetime.date.today(),
        user=saved_users["user_2"]
    )

    meal_plan_for_user_3 = MealPlan(
        title="Buttermilk Pancake, prepared from recipe",
        type=1,
        calories=86,
        diet=10,
        date=datetime.date.today(),
        user=saved_users["user_3"]
    )