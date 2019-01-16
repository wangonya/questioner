from werkzeug.exceptions import HTTPException


class UserAlreadyExistsError(HTTPException):
    """handle duplicate user registration"""


class InvalidEmailFormatError(HTTPException):
    """handle invalid format"""


class UserLoginError(HTTPException):
    """hanle invalid login details"""


class DataIndexError(HTTPException):
    """handle data not found errors"""


class AdminProtectedError(HTTPException):
    """handle unauthorised access"""


class InvalidPasswordLengthError(HTTPException):
    """handle password length during signup"""


class DuplicateDataError(HTTPException):
    """handle duplcate data entry"""


class InvalidRsvpStatusError(HTTPException):
    """handle invalid rsvp status"""


class InvalidMeetupIdError(HTTPException):
    """handle invalid meetup id"""


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
    "InvalidRsvpStatusError": {
        "message": "Rsvp status can only be 'yes', 'no' or 'maybe'",
        "status": 400,
    },
    "InvalidMeetupIdError": {
        "message": "Meetup id in url does not match id in body",
        "status": 400,
    }
}
