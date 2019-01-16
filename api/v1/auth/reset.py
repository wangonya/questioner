import re

from flask_restful import Resource, reqparse

from api.v1.utils.error_handlers import DataIndexError, InvalidEmailFormatError
from ..auth.models import AuthModel


class Reset(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @staticmethod
    def post():
        data = Reset.parser.parse_args()

        # check that email is in a correct format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
            raise InvalidEmailFormatError

        if AuthModel.find_by_email(data["email"]):

            response = {
                "status": 200,
                "message": "password reset instructions have been sent to your email",
                "data": [{
                    "email": data["email"]
                }]}

            return response, 200
        else:
            raise DataIndexError
