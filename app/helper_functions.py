from flask import jsonify, abort, make_response
from app import db

def verify_username_presence(cls, username):
    username_unavailable = db.session.query(cls.username).filter_by(username=username).first() is not None

    if username_unavailable:
        create_error_message("Username already in use. Try creating an account with a different username.", 400)


def verify_email_presence(cls, email):
    email_unavailable = db.session.query(cls.email).filter_by(email=email).first() is not None

    if email_unavailable:
        create_error_message("Email already in use. Try using a different email.", 400)

    if "@" not in email:
        create_error_message("Invalid email entered. Please enter a valid email.", 400)


def create_user_safely(cls, data_dict):
    # check if required attributes exist
    required_attributes = {"username", "first_name", "last_name", "email"}
   
    for attribute in required_attributes:
        if attribute not in data_dict:
            # multiple attributes can be missing, error message does not account for that
            create_error_message("Error, input is missing.", 400)
    
    # CHECK THAT USERNAME AND EMAIL NOT ALREADY IN DB
    verify_username_presence(cls, data_dict["username"])
    verify_email_presence(cls, data_dict["email"])

    # Create the user if the username and email does not exist already
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


def create_success_message(message, status_code=200):
    return make_response(jsonify(message), status_code)