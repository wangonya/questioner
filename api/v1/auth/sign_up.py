from flask import request, abort, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from v1.auth import models
import re
import datetime as date

sign_up = Blueprint('sign_up', __name__, url_prefix='/api/v1/auth')


@sign_up.route('/signup', methods=['POST'])
def user_signup():

    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        othername = request.json['othername']
        email = request.json['email']
        phonenumber = request.json['phoneNumber']
        password = request.json['password']
        isadmin = request.json['isAdmin']

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
            try:
                u_id = models.users[-1]['id'] + 1
            except IndexError:
                u_id = 1
            user = {
                'id': u_id,
                'email': email,
                'password': generate_password_hash(password),
                'firstname': firstname,
                'lastname': lastname,
                'othername': othername,
                'phoneNumber': phonenumber,
                'username': email.split('@')[0],
                'registered': date.datetime.now(),
                'isAdmin': isadmin
            }
            models.users.append(user)
            access_token = create_access_token(identity=email)
            return jsonify(
                {
                    "status": 201,
                    "data": [{
                        "msg": "user registered successfully",
                        "user": user,
                        "access_token": access_token
                    }]
                }), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
