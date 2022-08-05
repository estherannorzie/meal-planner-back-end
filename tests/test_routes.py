def test_get_all_users_with_no_records(client):
    # Act
    response = client.get("/users")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_create_one_user(client):
     # Act
    response = client.post("/users", json={
        "username": "Tamara_Tromp36",
        "first_name": "Elmore",
        "last_name": "Shanahan",
        "email": "Kadin69@gmail.com"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "User Tamara_Tromp36 successfully created."


def test_get_all_users_with_records(client, saved_users):
    # Act
    response = client.get("/users")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "username": "eggpioneer10",
            "first_name": "Vance",
            "last_name": "Lehner",
            "email": "Vance.Lehner90@gmail.com"
        },
        {
            "id": 2,
            "username": "fishalienpie",
            "first_name": "Lora",
            "last_name": "Kassulke",
            "email": "Lora.Kassulke75@yahoo.com"
        },
        {
            "id": 3,
            "username": "nailspotato",
            "first_name": "Katelin",
            "last_name": "Gulgowski",
            "email": "Katelin_Gulgowski94@hotmail.com"
        }
    ]


def test_get_one_user(client, saved_users):
    # Act
    response = client.get("/users/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "username": "eggpioneer10",
        "first_name": "Vance",
        "last_name": "Lehner",
        "email": "Vance.Lehner90@gmail.com"
    }


def test_update_user_email(client, saved_users):
    response = client.patch("/users/1", json={
        "email": "Oliver_Roberts33@hotmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User eggpioneer10 email updated to Oliver_Roberts33@hotmail.com"


def test_update_user_email_only_email_present(client, saved_users):
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


def test_delete_user(client, saved_users):
    response = client.delete("/users/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User fishalienpie successfully deleted."


def test_delete_nonexistent_user(client, saved_users):
    response = client.delete("/users/1000")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User does not exist."


def test_delete_invalid_user(client):
    response = client.delete("/users/1o")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "The User ID is not a valid ID."