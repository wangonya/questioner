from flask import request, abort, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from v1.auth import models
import re

sign_up = Blueprint('sign_up', __name__, url_prefix='/api/v1/auth')


@sign_up.route('/signup', methods=['POST'])
def user_signup():

    try:
        email = request.json['email']
        password = request.json['password']

        # check if email already exists to avoid duplicates
        if any(u['email'] == email for u in models.users):
            return jsonify(
                {
                    "status": 409,
                    "error": "email already exists"
                }), 409

        # check that data is in a correct format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return jsonify(
                {
                    "status": 400,
                    "error": "email format invalid"
                }), 400
        elif 6 > len(password) or 12 < len(password):
            return jsonify(
                {
                    "status": 422,
                    "error": "password length invalid"
                }), 422
        else:
            user = {
                'email': email,
                'password': generate_password_hash(password)
            }
            models.users.append(user)
            return jsonify(
                {
                    "status": 201,
                    "data": [{
                        "msg": "user registered successfully",
                        "email": email
                    }]
                }), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
