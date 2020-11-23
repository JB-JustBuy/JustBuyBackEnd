from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository


class Login(Resource):
    def __init__(self, **kwargs):
        self.rp_config = kwargs["repository"]
        self.rp = UserRepository(self.rp_config)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("account", required=True, help='account is required')
        parser.add_argument("password", required=True, help='password is required')
        arg = parser.parse_args()
        print('arg', arg)
        data = {
            'account': arg['account'],
            'password': arg['password']
        }

        res = self.rp.login(data)
        return {
            "message": 'success',
            "res": res
        }, 200