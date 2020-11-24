import re
from flask_login import UserMixin
from src.repository.user_respository import UserRepository
from src.repository.config import USER_REPOSITORY_CONFIG
class User(UserMixin):

    @staticmethod
    def validate_format(data: dict) -> list:
        check_username_result = User.validate_username(data['username'])
        check_email_result = User.validate_email(data['email'])
        check_password_result = User.validate_password(data['password'])
        check_confirm_password_result = User.validate_confirm_password(data['password'], data['confirmPassword'])
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

    @staticmethod
    def get(email):
        rp = UserRepository(USER_REPOSITORY_CONFIG)
        users = rp.get_users()
        for index, user in enumerate(users):
            if email == user['email']:
                return users[index]
        return None