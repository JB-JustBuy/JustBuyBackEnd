from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository
from src.entities.user.user import User

class SignUpController(Resource):
    def __init__(self, **kwargs):
        self.rp_config = kwargs["repository"]
        self.rp = UserRepository(self.rp_config)

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
        parser.add_argument('confirmPassword', required=True, help="confirmPassword is required.")
        arg = parser.parse_args()
        data = {
            "document": {
                "username": arg["username"],
                "email": arg['email'],
                "password": arg["password"],
                'confirmPassword': arg['confirmPassword']
            }
        }

        is_exist = self.is_exist(data)
        is_format_correct = User.validate_format(data)
        message = is_exist + is_format_correct
        status = 'success' if message == [] else 'failed'

        return {
            "message": "success",
            "res": {
                'status': status,
                'message': message
            }
        }, 200


