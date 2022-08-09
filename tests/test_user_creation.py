def test_create_one_user(client):
    response = client.post("/users", json={
        "username": "Tamara_Tromp36",
        "password": "^2OxH4H0la!h",
        "first_name": "Elmore",
        "last_name": "Shanahan",
        "email": "Kadin69@gmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "User Tamara_Tromp36 successfully created."


def test_user_creation_aborts_if_missing_password(client):
    response = client.post("/users", json={
        "username": "Dogbunny54",
        "first_name": "Adrianna",
        "last_name": "Kuhlman",
        "email": "Adrianna_Kuhlman@hotmail.com"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Username, first name, last name, password, and email are required. Try again."


def test_user_creation_aborts_if_unneeded_properties_present(client):
    response = client.post("/users", json={
        "username": "LinkLearner",
        "password": "^2OxH4H0la!h",
        "first_name": "Adrianna",
        "last_name": "Kuhlman",
        "email": "Adrianna_Kuhlman@hotmail.com",
        "DOB": "1997/10/21"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "Additional unneeded attributes submitted. Try again."


def test_user_creation_aborts_if_username_in_use(client, saved_users):
    response = client.post("/users", json={
        "username": "nailspotato",
        "password": "^2OxH4H0la!h",
        "first_name": "Garry",
        "last_name": "Abernathy",
        "email": "Garry_Abernathy52@yahoo.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "An integrity error occurred."


def test_user_creation_aborts_if_email_in_use(client, saved_users):
    response = client.post("/users", json={
        "username": "DoneDynasty097",
        "password": "^2OxH4H0la!h",
        "first_name": "Erin",
        "last_name": "Patton",
        "email": "Katelin_Gulgowski94@hotmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "An integrity error occurred."


def test_user_creation_aborts_if_username_too_long(client):
    response = client.post("/users", json={
        "username": "a_veryveryveryveryveryveryveryveryveryveryvveryveryveryveryveryveryveryveryveryverylong_username",
        "password": "^2OxH4H0la!h",
        "first_name": "Darron",
        "last_name": "Holt",
        "email": "Darron_Holt40@gmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "A data error occurred."


def test_user_creation_aborts_if_email_too_long(client):
    response = client.post("/users", json={
        "username": "HolyTyphoon439",
        "password": "^2OxH4H0la!h",
        "first_name": "Darron",
        "last_name": "Holt",
        "email": "a_veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylong_email@gmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "A data error occurred."


def test_user_creation_aborts_if_first_name_too_long(client):
    response = client.post("/users", json={
        "username": "HolyTyphoon439",
        "password": "^2OxH4H0la!h",
        "first_name": "a_long_first_name",
        "last_name": "Holt",
        "email": "Darron_Holt40@gmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "A data error occurred."


def test_user_creation_aborts_if_last_name_too_long(client):
    response = client.post("/users", json={
        "username": "HolyTyphoon439",
        "password": "^2OxH4H0la!h",
        "first_name": "Darron",
        "last_name": "a__long_last_name",
        "email": "Darron_Holt40@gmail.com",
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "A data error occurred."