from flask import jsonify, abort, make_response
from app import db

def check_if_username_email_is_present(cls, data_dict):
    username_exists = db.session.query(cls.username).filter_by(username=data_dict["username"]).first() is not None

    email_exists = db.session.query(cls.email).filter_by(email=data_dict["email"]).first() is not None

    if username_exists and email_exists:
        create_error_message("Username and email address already in use. Try creating an account with a different username and email.", 400)

    if username_exists:
        create_error_message("Username already in use. Try creating an account with a different username.", 400)

    if email_exists:
        create_error_message("Email already in use. Try creating an account with a different email.", 400)


def create_user_safely(cls, data_dict):
    # check if required attributes exist
    required_attributes = {"username", "first_name", "last_name", "email"}
   
    for attribute in required_attributes:
        if attribute not in data_dict:
            create_error_message("Error, input is missing.", 400)
    
    check_if_username_email_is_present(cls, data_dict)

    return cls.from_dict(data_dict)


def get_record_by_id(cls, id):
    try:
        id = int(id)
    except ValueError:
        create_error_message(f"User id: {id} is not a valid id.", 400)
    record = cls.query.get(id)

    if record:
        return record
    else:
        create_error_message(f"User id: {id} does not exist.", 404)


def create_error_message(message, status_code):
    abort(make_response(jsonify({"details": message}), status_code))


def create_success_message(message, status_code):
    make_response(jsonify({"details": message}), status_code)