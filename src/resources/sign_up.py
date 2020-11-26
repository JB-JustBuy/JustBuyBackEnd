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


        try:
            user = UserRepository(username=data['username'],
                            email=data['email'],
                            password=data['password'])
            user.check_confirm_password(data['confirmPassword'])
            user.hash_password()
            user.save()
            id = str(user.id)
            message = "success"
        except Exception as e:
            message = e.args[0]
            id = None

        return make_response({
            "message": message,
            "id": id
            }, 200)


