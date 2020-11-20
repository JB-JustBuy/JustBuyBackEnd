from flask_restful import Resource, reqparse
from src.repository.repository import Repository


class SignUpController(Resource):
    def __init__(self, **kwargs):
        self.rp_config = kwargs["repository"]
        self.rp = Repository(self.rp_config)

    def get(self):
        response = self.rp.read()
        return {
            "message": "success",
            "response": response
        }, 200

    def post(self,):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="username is required.")
        parser.add_argument('email', required=True, help="email is required.")
        parser.add_argument('password', required=True, help="password is required.")
        parser.add_argument('confirmPassword', required=True, help="password is required.")
        arg = parser.parse_args()
        data = {
            "document": {
                "account": arg["username"],
                "email": arg['email'],
                "password": arg["password"],
                'confirmPassword': arg['confirmPassword']
            }
        }
        response = self.rp.write(data)

        return {
            "message": "success",
            "res": response
        }, 200


