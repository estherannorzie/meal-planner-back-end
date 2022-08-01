from flask import jsonify, abort, make_response
from app import db

def verify_username_presence(cls, username):
    username_unavailable = db.session.query(cls.username).filter_by(username=username).first() is not None

    if username_unavailable:
        create_error_message("Username already in use. Try creating an account with a different username.", 400)

def validate_email_update_request(data_dict):
    if len(data_dict) > 1:
        create_error_message("Too many properties submitted. Try again.", 400)

    if "email" not in data_dict:
        create_error_message("Email not in request. Try again.", 400)


def verify_email_presence(cls, email):
    email_unavailable = db.session.query(cls.email).filter_by(email=email).first() is not None

    if email_unavailable:
        create_error_message("Email already in use. Try using a different email.", 400)

    if "@" not in email:
        create_error_message("Invalid email entered. Please enter a valid email.", 400)


def create_user_safely(cls, data_dict):
    # check if required attributes exist
    required_attributes = {"username", "first_name", "last_name", "email"}

    if len(data_dict) > len(required_attributes):
        create_error_message("Too many properties submitted. Try again.", 400)
   
    for attribute in required_attributes:
        if attribute not in data_dict:
            # multiple attributes can be missing, error message does not account for that
            create_error_message(f"Error, {attribute} is missing.", 400)
    
    # CHECK THAT USERNAME AND EMAIL NOT ALREADY IN DB
    verify_username_presence(cls, data_dict["username"])
    verify_email_presence(cls, data_dict["email"])

    # Create the user if the username and email does not exist already
    return cls.from_dict(data_dict)


def get_record_by_id(cls, id):
    try:
        id = int(id)
    except ValueError:
        create_error_message(f"{cls} ID: {id} is not a valid ID.", 400)
    record = cls.query.get(id)

    if not record:
        create_error_message(f"{cls} ID: {id} does not exist.", 404)

    return record 


def verify_meal_plan_presence(cls, title):
    meal_plan_unavailable = db.session.query(cls.title).filter_by(title=title).first() is not None

    if meal_plan_unavailable:
        create_error_message("You have already added this meal plan.", 400)


def create_meal_plan_safely(cls, data_dict, user):
    if "title" not in data_dict or "type" not in data_dict:
        create_error_message("Missing required attribute(s).", 400)

    # check that the meal plan is not present for user
    verify_meal_plan_presence(cls, data_dict["title"])
    
    # now we can assume the required attributes exist...
    # if a key is not calories or diet abort

    possible_attributes = {"title", "type", "calories", "diet"}
    submitted_attributes = set(data_dict.keys())

    if not submitted_attributes.issubset(possible_attributes):
        create_error_message("Incorrect attribute submitted. Try again.", 400)

    # Create the meal plan for the user
    return cls.from_dict(data_dict, user)


def create_error_message(message, status_code):
    abort(make_response(jsonify({"details": message}), status_code))


def create_success_message(message, status_code=200):
    return make_response(jsonify(message), status_code)