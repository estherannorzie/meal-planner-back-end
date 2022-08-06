from datetime import date

def test_update_user_meal_plan(client, saved_users_meal_plans):
    response = client.put("/users/1/meal_plans/1", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User eggpioneer10's meal plan updated to Easy Meatloaf successfully."


def test_user_cannot_update_meal_plan_without_title(client, saved_users_meal_plans):
    response = client.put("/users/1/meal_plans/1", json={
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Missing title."


def test_user_cannot_update_meal_plan_without_type(client, saved_users_meal_plans):
    response = client.put("/users/1/meal_plans/1", json={
        "title": "Easy Meatloaf",
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Missing type."


def test_invalid_user_cannot_update_meal_plan(client, saved_users_meal_plans):
    response = client.put("/users/1o/meal_plans/1", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "User ID: 1o is not a valid ID."


def test_nonexistent_user_cannot_update_meal_plan(client, saved_users_meal_plans):
    response = client.put("/users/4/meal_plans/1", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 4 does not exist."


def test_user_cannot_update_invalid_meal_plan(client, saved_users_meal_plans):
    response = client.put("/users/3/meal_plans/E", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Meal plan ID: E is not a valid ID."


def test_user_cannot_update_nonexistent_meal_plan(client, saved_users_meal_plans):
    response = client.put("/users/3/meal_plans/4", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date.today().strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Meal plan ID: 4 does not exist."


def test_user_cannot_update_meal_plan_date_to_past(client, saved_users_meal_plans):
    response = client.put("/users/3/meal_plans/1", json={
        "title": "Easy Meatloaf",
        "type": 4,
        "calories": 372,
        "date": date(2000, 1, 1).strftime("%Y-%m-%d")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Meal plans cannot be created or updated to the past."