from flask import jsonify, abort, make_response

def create_user_safely(cls, data_dict):
    # iterate through username column
    # if the username is equal to the user's username input abort message
    # iterate through email column
    # if the email is equal to the user's email input abort message
    pass