def test_get_all_users_with_no_records(client):
    # Act
    response = client.get("/users")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


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