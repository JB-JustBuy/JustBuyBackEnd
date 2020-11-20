from src.repository.repository import Repository
import re


class UserRepository(Repository):
    def __init__(self, data):
        super().__init__(data)

    def is_exist(self, data):
        res = self.collection.find(data)
        print("res", res)
        return True if res else False

    def validate_format(self, data:dict) -> dict:
        check_username_result = self.__validate_username(data['username'])
        check_email_result = self.__validate_email(data['email'])
        check_password_result = self.__validate_password(data['password'])
        check_confirm_password_result = self.__validate_confirm_password(data['password'], data['confirmPassword'])
        message = check_username_result + check_email_result + check_password_result + check_confirm_password_result
        status = "success" if message == [] else 'failed'
        return {
            'status': status,
            'message': message
        }

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
