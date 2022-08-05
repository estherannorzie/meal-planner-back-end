import pytest
import datetime

def test_create_one_user_meal_plan(client, saved_users, saved_users_meal_plans):
     # Act
    response = client.post("/users/1/meal_plans", json={
        "title": "Krispy Kreme Doughnuts Original Glazed Doughnut",
        "type": 4,
        "calories": 190,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Krispy Kreme Doughnuts Original Glazed Doughnut meal plan for user eggpioneer10 successfully created."


def test_creating_user_meal_plan_aborts_if_meal_plan_already_exists(client, saved_users, saved_users_meal_plans):
    response = client.post("/users/2/meal_plans", json={
        "title": "Spaghetti & Meatballs with Tomato Sauce, small",
        "type": 3,
        "calories": 412,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Duplicate meal plans are not allowed."

@pytest.mark.skip(reason="Do later")
def test_user_cannot_create_past_meal_plans(client, saved_users):
    pass

@pytest.mark.skip(reason="Do later")
def test_invalid_user_cannot_create_meal_plan(client, saved_users):
    pass

@pytest.mark.skip(reason="Do later")
def test_nonexistent_user_cannot_create_meal_plan(client, saved_users):
    pass