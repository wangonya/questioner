from datetime import datetime
from werkzeug.security import generate_password_hash


class AuthModel:
    user_model = []

    def __init__(self, firstname, lastname, othername,
                 email, phonenumber, password):
        self.uid = len(AuthModel.user_model) + 1
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phonenumber = phonenumber
        self.othername = othername
        self.username = email.split('@')[0],
        self.password = generate_password_hash(password)
        self.isadmin = False
        self.registered = datetime.now()

    def save_to_db(self):
        AuthModel.user_model.append(self)

    @classmethod
    def find_by_email(cls, email):
        return any(u.email == email for u in AuthModel.user_model)
