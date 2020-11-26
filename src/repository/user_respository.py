from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import re


class UserRepository(db.Document):
    username = db.StringField(require=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)

    def check_confirm_password(self, confirm_password):
        raise Exception("confirmPassword and password are not the same")

    @staticmethod
    def get_users() -> list:
        users = UserRepository.objects()
        return users

    @staticmethod
    def validate_format(data: dict) -> list:
        check_username_result = UserRepository.validate_username(data['username'])
        check_email_result = UserRepository.validate_email(data['email'])
        check_password_result = UserRepository.validate_password(data['password'])
        check_confirm_password_result = UserRepository.validate_confirm_password(data['password'], data['confirmPassword'])
        message = check_username_result + check_email_result + check_password_result + check_confirm_password_result
        return message

    @staticmethod
    def validate_username(username: str) -> list:
        message = []
        if len(username) < 6:
            message.append('length of username needs to bigger than 6')
        if re.search(r"\W", username) is not None:
            message.append('username cant use symbol')
        return message

    @staticmethod
    def validate_email(email: str) -> list:
        message = []
        if "@" not in email or (".org" not in email and
                                '.com' not in email and
                                '.edu' not in email):
            print()
            message.append("email format error")
        return message

    @staticmethod
    def validate_password(password) -> list:
        message = []
        if len(password) < 8:
            message.append("length of password needs to bigger than 8")
        return message

    @staticmethod
    def validate_confirm_password(password, confirm_password):
        message = []
        if password != confirm_password:
            message.append('password and confirm password arent the same')
        return message