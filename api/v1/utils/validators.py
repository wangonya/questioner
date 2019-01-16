import re

from .error_handlers import (InvalidEmailFormatError, InvalidPasswordLengthError,
                             UserAlreadyExistsError, DuplicateDataError, InvalidRsvpStatusError,
                             InvalidMeetupIdError)
from ..auth.models import AuthModel
from ..meetups.models import MeetupModel, RsvpsModel
from ..questions.models import PostQuestionsModel, AnswerQuestionsModel


class AuthValidators:
    """validators for login, signup and reset password"""
    @staticmethod
    def check_email_format(email):
        """using regex to check email format"""
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise InvalidEmailFormatError

    @staticmethod
    def check_password_length(password):
        """check that password is appropriate length"""
        if len(password) < 6 or len(password) > 12:
            raise InvalidPasswordLengthError

    @staticmethod
    def check_email_exists(email):
        """check if email already exists to avoid duplicates"""
        if AuthModel.find_by_email(email):
            raise UserAlreadyExistsError


class MeetupValidators:
    """validators for post meetups and rsvps"""
    @staticmethod
    def check_duplicate_meetup(title, creator):
        """check if the same creator has entered a meetup with the same title"""
        if MeetupModel.find_duplicate_meetup(title, creator):
            raise DuplicateDataError


class QuestionValidators:
    """validators for posting question"""
    @staticmethod
    def check_duplicate_question(title, meetup):
        """check if the same question has been asked in the same meetup"""
        if PostQuestionsModel.find_duplicate_question(title, meetup):
            raise DuplicateDataError

    @staticmethod
    def check_meetup_id(body_id, url_id):
        """make sure meetup id passed in url matches meetup id in body"""
        if not body_id == url_id:
            raise InvalidMeetupIdError


class AnswerValidators:
    """validators for answering question"""
    @staticmethod
    def check_duplicate_answer(body, question):
        """check if a similar answer exists in the question"""
        if AnswerQuestionsModel.find_duplicate_answer(body, question):
            raise DuplicateDataError


class RsvpValidators:
    """validators for rsvps"""
    @staticmethod
    def check_proper_rsvp(status):
        """rsvp status should only be 'yes', 'no', or 'maybe'"""
        if status not in ("yes", "no", "maybe"):
            raise InvalidRsvpStatusError
