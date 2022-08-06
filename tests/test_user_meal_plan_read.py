from datetime import date

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
        "date": date.today(),
        "diet": None,
    },

    {
        "id": 2,
        "title": "Spaghetti & Meatballs with Tomato Sauce, small",
        "type": 3,
        "calories": 412,
        "date": date.today(),
        "diet": None,
    },

    {
        "id": 3,
        "title": "Buttermilk Pancake, prepared from recipe",
        "type": 1,
        "calories": 86,
        "date": date.today(),
        "diet": 10,
    }
]