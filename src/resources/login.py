from flask_restful import Resource, reqparse
from flask_login import logout_user, login_user
from src.repository.user_respository import UserRepository
from src.entities.user.user import User


class Login(Resource):
    def __init__(self, **kwargs):
        self.rp_config = kwargs["repository"]
        self.rp = UserRepository(self.rp_config)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", required=True, help='account is required')
        parser.add_argument("password", required=True, help='password is required')
        arg = parser.parse_args()
        print('arg', arg)
        data = {
            'email': arg['email'],
            'password': arg['password']
        }

        users = self.rp.get_users()
        message = 'bad login'
        if data['email'] in [user['email'] for user in users]:
            user = User()
            user.id = data['email']
            login_user(user)
            message = 'success'

        return {
            "message": message,
        }, 200