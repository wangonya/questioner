from flask import request, abort, jsonify, Blueprint
from api.v1.auth import models
import re

reset = Blueprint('reset', __name__, url_prefix='/api/v1/auth')


@reset.route('/reset', methods=['POST'])
def user_reset():

    try:
        email = request.json['email']

        # check that data is in a correct format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return jsonify(
                {
                    "status": 400,
                    "error": "email format invalid"
                }), 400
        if any(u['email'] == email for u in models.users):
            return jsonify(
                {
                    "status": 200,
                    "data": [{
                        "msg": "a reset link has been sent to your email",
                        "email": email
                    }]
                }), 200
        else:
            return jsonify(
                {
                    "status": 401,
                    "error": "that account does not exist"
                }), 401
    except (ValueError, KeyError, TypeError):
        abort(400)
