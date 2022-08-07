def test_update_user_email(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "Oliver_Roberts33@hotmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User eggpioneer10 email updated to Oliver_Roberts33@hotmail.com"


def test_updating_email_aborts_if_unneeded_properties_present(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "Oliver_Roberts33@hotmail.com",
        "food": "Is very tasty."
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Too many properties submitted. Try again."


def test_update_user_email_aborts_if_email_invalid(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "@hotmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "The email submitted is not a valid email. Try again."


def test_update_user_email_aborts_if_email_in_use(client, saved_users):
    response = client.patch("/users/3", json={
        "email": "Katelin_Gulgowski94@hotmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Email already in use. Try a different email."


def test_user_creation_aborts_if_email_too_long(client):
    response = client.post("/users", json={
        "username": "MartianToxin409",
        "first_name": "Aurelia",
        "last_name": "James",
        "email": "a_veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylong_email@gmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "An attribute is too long. Try again."