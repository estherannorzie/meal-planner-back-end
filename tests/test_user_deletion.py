def test_delete_user(client, saved_users):
    response = client.delete("/users/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "User fishalienpie successfully deleted."


def test_delete_nonexistent_user(client, saved_users):
    response = client.delete("/users/1000")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "User ID: 1000 does not exist."


def test_delete_invalid_user(client):
    response = client.delete("/users/1o")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == "User ID: 1o is not a valid ID."