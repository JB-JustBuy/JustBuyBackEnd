from flask import make_response, jsonify, session
from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository


class LoginController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", required=True, help='account is required')
        parser.add_argument("password", required=True, help='password is required')
        arg = parser.parse_args()
        data = {
            'email': arg['email'],
            'password': arg['password']
        }
        users = UserRepository.get_users()
        message = 'bad login'
        emails = [user.email for user in users]
        print("data['email'] ", data['email'])
        print("emails", emails)
        if data['email'] in emails:
            message = 'success'

        res = {
            "message": message,
        }
        return make_response(jsonify(res), 200)

    def get(self):
        session['key'] = 'test'
        res = {'message': 'ok'}
        return make_response(jsonify(res), 200)