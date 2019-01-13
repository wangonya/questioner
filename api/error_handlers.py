from werkzeug.exceptions import HTTPException


class UserAlreadyExistsError(HTTPException):
    pass


class InvalidEmailFormatError(HTTPException):
    pass


class UserLoginError(HTTPException):
    pass


class DataIndexError(HTTPException):
    pass


class AdminProtectedError(HTTPException):
    pass


errors = {
    "UserAlreadyExistsError": {
        "message": "A user with that email already exists",
        "status": 409,
    },
    "InvalidEmailFormatError": {
        "message": "Invalid email format",
        "status": 400,
    },
    "UserLoginError": {
        "message": "Incorrect login details",
        "status": 401,
    },
    "DataIndexError": {
        "message": "No data exists in the requested resource",
        "status": 404,
    },
    "AdminProtectedError": {
        "message": "Only admins can access this route",
        "status": 401,
    },
}
