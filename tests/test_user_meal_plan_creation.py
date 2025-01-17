from datetime import datetime, date, timezone

def test_create_one_user_meal_plan(client, saved_users):
    response = client.post("/users/1/meal_plans", json={
        "title": "Krispy Kreme Doughnuts Original Glazed Doughnut",
        "type": 4,
        "calories": 190,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Krispy Kreme Doughnuts Original Glazed Doughnut meal plan for user eggpioneer10 successfully created."


def test_creating_user_meal_plan_aborts_if_meal_plan_already_exists(client, saved_users, saved_users_meal_plans):
    response = client.post("/users/2/meal_plans", json={
        "title": "Spaghetti & Meatballs with Tomato Sauce, small",
        "type": 3,
        "calories": 412,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "An integrity error occurred."


def test_user_cannot_create_past_meal_plans(client, saved_users):
    response = client.post("/users/2/meal_plans", json={
        "title": "Frosted Flakes Ready-to-Eat Cereal",
        "type": 1,
        "calories": 143,
        "date": date(2000, 1, 1).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Meal plans cannot be created or updated to a past date."


def test_invalid_user_cannot_create_meal_plan(client, saved_users):
    response = client.post("/users/1oo/meal_plans", json={
        "title": "Sandwich, Ham (4 oz), Cheese (4 oz), mayo, 3 oz Bread",
        "type": 2,
        "calories": 800,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "User ID: 1oo is not a valid ID."


def test_nonexistent_user_cannot_create_meal_plan(client, saved_users):
    response = client.post("/users/5/meal_plans", json={
        "title": "Stuffed Zucchini",
        "type": 3,
        "calories": 570,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 5 does not exist."


def test_abort_user_meal_plan_creation_title_not_present(client, saved_users):
    response = client.post("/users/2/meal_plans", json={
        "type": 2,
        "calories": 800,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Missing title."


def test_abort_user_meal_plan_creation_type_not_present(client, saved_users):
    response = client.post("/users/2/meal_plans", json={
        "title": "Sandwich, Ham (4 oz), Cheese (4 oz), mayo, 3 oz Bread",
        "calories": 800,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Missing type."


def test_abort_user_meal_plan_creation_title_too_long(client, saved_users):
    response = client.post("/users/2/meal_plans", json={
        "title": "Stuffed Zucchini is Extremely Delicious, it will help me get my nutrition",
        "type": 3,
        "calories": 570,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT")
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "A data error occurred."