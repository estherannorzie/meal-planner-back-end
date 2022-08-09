from flask import jsonify, abort, make_response
from app import db
from sqlalchemy import exc
from datetime import datetime, timezone, date

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
    required_attributes = {"username", "password", "first_name", "last_name", "email"}

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
    
    confirm_proper_attributes_present(
        possible_attributes={"title", "type", "calories", "diet", "date"},
        submitted_attributes=set(data_dict.keys())
    )

    if "date" in data_dict:
        check_if_date_in_past(data_dict["date"])

    return cls.from_dict(data_dict, user)


def update_user_meal_plan_safely(cls, data_dict, meal_plan):
    verify_title_and_type(data_dict)

    confirm_proper_attributes_present(
        possible_attributes={"title", "type", "calories", "diet", "date"},
        submitted_attributes=set(data_dict.keys())
    )
    
    if "date" in data_dict:
        check_if_date_in_past(data_dict["date"])

    return cls.update_meal_plan(meal_plan, data_dict)


def check_if_date_in_past(str_date):
    date_object = datetime.now(timezone.utc).strptime(str_date, "%a, %d %b %Y %X GMT")

    if date_object.date() < date.today():
        create_error_message("Meal plans cannot be created or updated to a past date.")


def validate_update_user_request(data_dict, user):
    confirm_proper_attributes_present(
        possible_attributes={"password", "email"},
        submitted_attributes=set(data_dict.keys())
    )

    if "email" in data_dict:
        if data_dict["email"] == user.email:
            create_error_message("Email already in use. Try a different email.")
        verify_valid_email(data_dict["email"])


def validate_password_change(data_dict, user):
    pass


def confirm_proper_attributes_present(possible_attributes, submitted_attributes):
    if not submitted_attributes.issubset(possible_attributes):
        create_error_message("Incorrect attribute(s) submitted. Try again.")


def verify_title_and_type(data_dict):
    if "title" not in data_dict:
        create_error_message("Missing title.")

    if "type" not in data_dict:
        create_error_message("Missing type.")


def attempt_db_commit():
    try:
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        create_error_message("An integrity error occurred.")
    except exc.DataError:
        db.session.rollback()
        create_error_message("A data error occurred.")


def create_error_message(message, status_code=400):
    abort(make_response(jsonify(message), status_code))


def create_success_message(message, status_code=200):
    return make_response(jsonify(message), status_code)