from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository


class UserController(Resource):
    def get(self):
        users = UserRepository.get_users()
        return make_response(jsonify({
            'users': users
        }), 200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="username is required.")
        parser.add_argument('email', required=True, help="email is required.")
        parser.add_argument('password', required=True, help="password is required.")

        arg = parser.parse_args()
        data = {
            "username": arg["username"],
            "email": arg['email'],
            "password": arg["password"],
        }
        user = UserRepository(**data).save()
        return make_response(jsonify({
            'user': {
                "email": user.email
            }
        }), 200)



