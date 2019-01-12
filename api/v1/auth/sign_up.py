import re

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from ...error_handlers import UserAlreadyExistsError, InvalidEmailFormatError
from ..auth.models import AuthModel


class Signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("firstname",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("lastname",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("phonenumber",
                        type=str)
    parser.add_argument("othername",
                        type=str)

    @staticmethod
    def post():
        data = Signup.parser.parse_args()

        # check if email already exists to avoid duplicates
        if AuthModel.find_by_email(data["email"]):
            raise UserAlreadyExistsError

        # check that email is in a correct format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
            raise InvalidEmailFormatError
        
        user = AuthModel(**data)
        user.save_to_db()

        response = {
            "status": 201,
            "message": "user registered successfully",
            "data": [{
                "access_token": create_access_token(data["email"])
                }]}

        return response, 201
