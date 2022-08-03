from flask import jsonify, abort, make_response
from app import db

def get_record_by_id(cls, id):
    try:
        id = int(id)
    except ValueError:
        create_error_message(f"{cls.stringify()} ID: {id} is not a valid ID.", 400)
    record = cls.query.get(id)

    if not record:
        create_error_message(f"{cls.stringify()} ID: {id} does not exist.", 404)

    return record 


def create_user_safely(cls, data_dict):
    required_attributes = {"username", "first_name", "last_name", "email"}

    if len(data_dict) > len(required_attributes):
        create_error_message("Additional unneeded attributes submitted. Try again.")

    if len(data_dict) != len(required_attributes):
        create_error_message("Username, first name, last name and email are required. Try again.")
    
    verify_username_presence(cls, data_dict["username"])
    verify_email_presence(cls, data_dict["email"])

    return cls.from_dict(data_dict)


def create_user_meal_plan_safely(cls, data_dict, user):
    check_for_title_and_type(data_dict)

    verify_meal_plan_presence(cls, data_dict["title"])
    
    is_subset(submitted_attributes=set(data_dict.keys()))

    return cls.from_dict(data_dict, user)


def update_user_meal_plan_safely(cls, data_dict, meal_plan):
    check_for_title_and_type(data_dict)

    is_subset(submitted_attributes=set(data_dict.keys()))

    return cls.update_meal_plan(meal_plan, data_dict)


def verify_username_presence(cls, username):
    username_unavailable = db.session.query(cls.username).filter_by(username=username).first() is not None

    if username_unavailable:
        create_error_message("Username already in use. Try creating an account with a different username.")


def verify_email_presence(cls, email):
    email_unavailable = db.session.query(cls.email).filter_by(email=email).first() is not None

    if email_unavailable:
        create_error_message("Email already in use. Try using a different email.")

    if "@" not in email:
        create_error_message("Invalid email entered. Please enter a valid email.")


def verify_meal_plan_presence(cls, title):
    meal_plan_present = db.session.query(cls.title).filter_by(title=title).first() is not None

    if meal_plan_present:
        create_error_message("You have already added this meal plan.")


def validate_email_update_request(data_dict):
    if len(data_dict) > 1:
        create_error_message("Too many properties submitted. Try again.")

    if "email" not in data_dict:
        create_error_message("Email not in request. Try again.")


def is_subset(submitted_attributes):
    possible_attributes = {"title", "type", "calories", "diet"}

    if not submitted_attributes.issubset(possible_attributes):
        create_error_message("Incorrect attribute(s) submitted. Try again.")


def check_for_title_and_type(data_dict):
    if "title" not in data_dict or "type" not in data_dict:
        create_error_message("Missing title.")
    if "type" not in data_dict:
        create_error_message("Missing type.")


def create_error_message(message, status_code=400):
    abort(make_response(jsonify({"details": message}), status_code))


def create_success_message(message, status_code=200):
    return make_response(jsonify(message), status_code)