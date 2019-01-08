from flask import request, abort, jsonify, Blueprint
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from v1.auth import models
import re

log_in = Blueprint('log_in', __name__, url_prefix='/api/v1/auth')


@log_in.route('/login', methods=['POST'])
def user_login():

    try:
        email = request.json['email']
        password = request.json['password']

        # check that data is in a correct format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return jsonify(
                {
                    "status": 400,
                    "error": "email format invalid"
                }), 400
        if any(u['email'] == email for u in models.users):
            get_user_password = [u['password'] for u in models.users if u['email'] == email]
            if check_password_hash(get_user_password[0], password):
                access_token = create_access_token(identity=email)
                return jsonify(
                    {
                        "status": 200,
                        "data": [{
                            "msg": "user logged in successfully",
                            "email": email,
                            "access_token": access_token
                        }]
                    }), 200
            else:
                return jsonify(
                    {
                        "status": 401,
                        "error": "wrong password"
                    }), 401
        else:
            return jsonify(
                {
                    "status": 401,
                    "error": "that account does not exist"
                }), 401
    except (ValueError, KeyError, TypeError):
        abort(400)
