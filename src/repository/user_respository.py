from src.repository.repository import Repository
import re

class UserRepository(Repository):
    def __init__(self, data):
        super().__init__(data)

    def add_user(self, data:dict) -> dict:
        message = []
        check_username_result = self._validate_username(data['username'])
        return {
            'status': "failed",
            'message': message
        }, 200

    def __validate_username(self, username: str) -> list:
        message = []
        if len(username) < 6:
            message.append('length of username needs to bigger than 6')
        if re.search(r"\W", username) is not None:
            message.append('username cant use symbol')
        return message

    def __validate_email(self, email:str) -> list:
        message = []
        if "@" not in email or (".org" not in email and
                                '.com' not in email and
                                '.edu' not in email):
            message.append("email format error")
        return message

    def __validate_password(self, password) -> list:
        message = []
        if len(password) < 8:
            message.append("length of password needs to bigger than 8")
        return message

    def __validate_confirm_password(self, password, confirm_password):
        message = []
        if password != confirm_password:
            message.append('password and confirm password arent the same')
        return message
