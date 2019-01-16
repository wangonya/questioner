from werkzeug.exceptions import HTTPException


class UserAlreadyExistsError(HTTPException):
    """handle duplicate user registration"""
    pass


class InvalidEmailFormatError(HTTPException):
    """handle invalid format"""
    pass


class UserLoginError(HTTPException):
    """hanle invalid login details"""
    pass


class DataIndexError(HTTPException):
    """handle data not found errors"""
    pass


class AdminProtectedError(HTTPException):
    """handle unauthorised access"""
    pass


class InvalidPasswordLengthError(HTTPException):
    """handle password length during signup"""
    pass


class DuplicateDataError(HTTPException):
    """handle duplcate data entry"""
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
    "InvalidPasswordLengthError": {
        "message": "Invalid password length",
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
    "DuplicateDataError": {
        "message": "The data entered already exists in the resource",
        "status": 409,
    },
}
