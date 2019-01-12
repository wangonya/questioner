from werkzeug.exceptions import HTTPException


class UserAlreadyExistsError(HTTPException):
    pass


class InvalidEmailFormatError(HTTPException):
    pass


errors = {
    "UserAlreadyExistsError": {
        "error": "A user with that email already exists",
        "status": 409,
    },
    "InvalidEmailFormatError": {
        "error": "Invalid email format",
        "status": 400,
    },
}
