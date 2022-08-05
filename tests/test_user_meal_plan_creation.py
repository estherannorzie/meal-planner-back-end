import pytest
import datetime

def test_create_one_user_meal_plan(client, saved_users, saved_users_meal_plans):
     # Act
    response = client.post("/users/1/meal_plans", json={
        "title": "Oscar Mayer Extra Cheesy Pizza Lunchables",
        "type": 4,
        "calories": 280,
        "date": datetime.date.today()
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Meal_plan Oscar Mayer Extra Cheesy Pizza Lunchables for user eggpioneer10 successfully created."


@pytest.mark.skip(reason="No way to test this feature yet")
def test_creating_user_meal_plan_aborts_if_meal_plan_already_created(client, saved_users):
    pass