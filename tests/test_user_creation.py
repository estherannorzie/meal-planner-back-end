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


def test_user_creation_aborts_if_missing_property(client):
    response = client.post("/users", json={
        "first_name": "Adrianna",
        "last_name": "Kuhlman",
        "email": "Adrianna_Kuhlman@hotmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Username, first name, last name and email are required. Try again."


def test_user_creation_aborts_if_unneeded_properties_present(client):
    response = client.post("/users", json={
        "username": "LinkLearner",
        "first_name": "Adrianna",
        "last_name": "Kuhlman",
        "email": "Adrianna_Kuhlman@hotmail.com",
        "DOB": "1997/10/21"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Additional unneeded attributes submitted. Try again."