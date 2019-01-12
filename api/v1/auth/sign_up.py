from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

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
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("othername",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("isadmin",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @staticmethod
    def post():
        data = Signup.parser.parse_args()

        if AuthModel.find_by_email(data["email"]):
            response = {
                "status": 409,
                "error": "A user with that email already exists"
                }

            return response, 409
        
        user = AuthModel(**data)
        user.save_to_db()

        response = {
            "status": 201,
            "message": "user registered successfully",
            "data": [{
                "access_token": create_access_token(data["email"])
                }]}

        return response, 201
