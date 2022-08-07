from datetime import datetime, timezone

def test_read_user_meal_plan(client, saved_users_meal_plans):
    response = client.get("/users/1/meal_plans")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
    {
        "id": 1,
        "title": "Oscar Mayer Extra Cheesy Pizza Lunchables",
        "type": 4,
        "calories": 280,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT"),
        "diet": None,
    },

    {
        "id": 2,
        "title": "Spaghetti & Meatballs with Tomato Sauce, small",
        "type": 3,
        "calories": 412,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT"),
        "diet": None,
    },

    {
        "id": 3,
        "title": "Buttermilk Pancake, prepared from recipe",
        "type": 1,
        "calories": 86,
        "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %X GMT"),
        "diet": 10,
    }
]


def test_invalid_user_cannot_read_meal_plan(client, saved_users):
    response = client.get("/users/1oo/meal_plans")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "User ID: 1oo is not a valid ID."


def test_nonexistent_user_cannot_create_meal_plan(client, saved_users):
    response = client.get("/users/4/meal_plans")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 4 does not exist."