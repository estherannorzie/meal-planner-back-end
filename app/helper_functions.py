from flask import jsonify, abort, make_response
import datetime

def get_record_by_id(cls, id):
    try:
        id = int(id)
    except ValueError:
        create_error_message(f"The {cls.stringify()} ID is not a valid ID.", 400)
    record = cls.query.get(id)

    if not record:
        create_error_message(f"{cls.stringify()} does not exist.", 404)

    return record 


def create_user_safely(cls, data_dict):
    required_attributes = {"username", "first_name", "last_name", "email"}

    if len(data_dict) > len(required_attributes):
        create_error_message("Additional unneeded attributes submitted. Try again.")

    if len(data_dict) != len(required_attributes):
        create_error_message("Username, first name, last name and email are required. Try again.")

    verify_valid_email(data_dict["email"])
    
    return cls.from_dict(data_dict)


def verify_valid_email(email):
    if email[0] == "@" or "@" not in email:
        create_error_message("The email submitted is not a valid email. Try again.")


def create_user_meal_plan_safely(cls, data_dict, user):
    verify_title_and_type(data_dict)
    
    is_subset(submitted_attributes=set(data_dict.keys()))

    date_object = datetime.datetime.strptime(data_dict["date"], "%Y-%m-%d")

    if date_object.date() < datetime.date.today():
        create_error_message("Meal plans cannot be created in the past.")

    return cls.from_dict(data_dict, user)


def update_user_meal_plan_safely(cls, data_dict, meal_plan):
    verify_title_and_type(data_dict)

    verify_valid_email(data_dict["email"])

    is_subset(submitted_attributes=set(data_dict.keys()))

    return cls.update_meal_plan(meal_plan, data_dict)


def validate_email_update_request(data_dict):
    if len(data_dict) > 1:
        create_error_message("Too many properties submitted. Try again.")

    if "email" not in data_dict:
        create_error_message("Email not in request. Try again.")
    
    verify_valid_email(data_dict["email"])


def is_subset(submitted_attributes):
    possible_attributes = {"title", "type", "calories", "diet", "date"}

    if not submitted_attributes.issubset(possible_attributes):
        create_error_message("Incorrect attribute(s) submitted. Try again.")


def verify_title_and_type(data_dict):
    if "title" not in data_dict:
        create_error_message("Missing title.")

    if "type" not in data_dict:
        create_error_message("Missing type.")


def create_error_message(message, status_code=400):
    abort(make_response(jsonify(message), status_code))


def create_success_message(message, status_code=200):
    return make_response(jsonify(message), status_code)