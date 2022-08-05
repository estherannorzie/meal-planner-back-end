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


@pytest.mark.skip(reason="No way to test this feature yet")
def test_creating_user_meal_plan_aborts_if_meal_plan_already_created(client, saved_users):
    pass