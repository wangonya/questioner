from flask import request, abort, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from v1.auth import models
import re

sign_up = Blueprint('sign_up', __name__, url_prefix='/api/v1/auth')


@sign_up.route('/signup', methods=['POST'])
def user_signup():
    # make sure there's data and its properly formatted
    if None or not request.json:
        abort(400)

    email = request.json['email']
    password = request.json['password']

    # check if email already exists to avoid duplicates
    if any(u['email'] == email for u in models.users):
        return jsonify({'msg': 'email already exists'}), 409

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({'msg': 'email format invalid'}), 400
    elif 6 > len(password) or 12 < len(password):
        return jsonify({'msg': 'password length invalid'}), 422
    else:
        user = {
            'email': email,
            'password': generate_password_hash(password)
        }
        models.users.append(user)
        return jsonify({'user': user}), 201
