from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from api.v1.utils.validators import AuthValidators
from api.v1.utils.error_handlers import UserLoginError
from api.v1.auth.models import AuthModel


class Login(Resource):
    """login endpoint"""
    parser = reqparse.RequestParser()
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @staticmethod
    def post():
        """do a POST to resource"""
        data = Login.parser.parse_args()

        # check that email is in a correct format
        AuthValidators.check_email_format(data["email"])

        # verify password hash
        password = AuthModel.verify_hash(data["email"], data["password"])

        if AuthModel.find_by_email(data["email"]) and password:

            response = {
                "status": 200,
                "message": "user logged in successfully",
                "data": [{
                    "access_token": create_access_token(data["email"])
                }]}

            return response, 200
        else:
            raise UserLoginError
