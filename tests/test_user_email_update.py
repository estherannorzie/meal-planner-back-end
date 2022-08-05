def test_update_user_email(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "Oliver_Roberts33@hotmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User eggpioneer10 email updated to Oliver_Roberts33@hotmail.com"


def test_updating_email_aborts_if_unneeded_key_submitted(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "Oliver_Roberts33@hotmail.com",
        "food": "Is very tasty."
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Too many properties submitted. Try again."


def test_update_user_email_is_valid(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "@hotmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "The email submitted is not a valid email. Try again."
