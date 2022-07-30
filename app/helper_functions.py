import email
from flask import jsonify, abort, make_response
from sqlalchemy import select

def create_user_safely(cls, data_dict):
    email_exists = select(cls).where(cls.email==data_dict[email]).exists()
    username_exists = select(cls).where(cls.username==data_dict[username]).exists()

    # if the username is equal to the user's username input abort message
    if email_exists or username_exists:
        create_error_message("Username or email already in use.", 400)
    else:
        return data_dict

def create_error_message(message, status_code):
    abort(make_response(jsonify({"message": message}), status_code))