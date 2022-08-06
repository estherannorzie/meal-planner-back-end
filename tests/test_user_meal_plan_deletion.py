def test_delete_user_meal_plan(client, saved_users_meal_plans):
    response = client.delete("/users/2/meal_plans/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User fishalienpie's meal plan Oscar Mayer Extra Cheesy Pizza Lunchables successfully deleted."


def test_abort_deleting_nonexistent_user_meal_plan(client, saved_users_meal_plans):
    response = client.delete("/users/3/meal_plans/4")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Meal plan ID: 4 does not exist."


def test_abort_deleting_invalid_user_meal_plan(client, saved_users_meal_plans):
    response = client.delete("/users/2/meal_plans/1o")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Meal plan ID: 1o is not a valid ID."


def test_abort_deleting_meal_plan_if_user_nonexistent(client, saved_users_meal_plans):
    response = client.delete("/users/4/meal_plans/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 4 does not exist."


def test_abort_deleting_meal_plan_if_user_nonexistent(client, saved_users_meal_plans):
    response = client.delete("/users/1000/meal_plans/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 1000 does not exist."