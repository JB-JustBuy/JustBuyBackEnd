from flask import make_response
from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository


class SignUpController(Resource):
    def post(self,):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="username is required.")
        parser.add_argument('email', required=True, help="email is required.")
        parser.add_argument('password', required=True, help="password is required.")
        parser.add_argument('confirmPassword', required=True, help="confirmPassword is required.")
        arg = parser.parse_args()
        data = {
            "username": arg["username"],
            "email": arg['email'],
            "password": arg["password"],
            'confirmPassword': arg['confirmPassword']
        }

        is_format_correct = UserRepository.validate_format(data)
        if is_format_correct == []:
            UserRepository(username=data['username'],
                            email=data['email'],
                            password=data['password']).save()
            message = "success"
        else:
            message = is_format_correct

        return make_response({
            "message": message
            }, 200)


