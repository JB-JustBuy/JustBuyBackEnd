from .db import db
from flask import session
from flask_bcrypt import generate_password_hash, check_password_hash
import re


class UserRepository(db.Document):
    username = db.StringField(require=True, min_lenght=6)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def check_confirm_password(password, confirm_password):
        if password != confirm_password:
            raise Exception("confirmPassword and password are not the same")
        else:
            return

    def save_session(self):
        session['id'] = str(self.id)
        session['username'] = self.username
        session['email'] = self.email

    @staticmethod
    def remove_session():
        session['id'] = ""
        session['username'] = ''
        session['email'] = ''

    @classmethod
    def get_user(cls, email):
        return UserRepository.objects.get(email=email)

    @classmethod
    def delete(cls, **kwargs):
        UserRepository.objects(kwargs).get()

    @staticmethod
    def validate_email(email: str) -> None:
        if "@" not in email or (".org" not in email and
                                '.com' not in email and
                                '.edu' not in email):
            raise ValueError("email format error")
        return

    @staticmethod
    def validate_password(password) -> None:
        if len(password) < 8:
            raise ValueError("length of password needs to bigger than 8")
        return