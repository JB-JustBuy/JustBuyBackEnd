from flask_restful import Resource, reqparse
from src.repository.user_respository import UserRepository
from src.utilies.abort_msg import abort_msg


class SignupApi(Resource):
    def post(self,):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="username is required.")
        parser.add_argument('email', required=True, help="email is required.")
        parser.add_argument('password', required=True, help="password is required.")
        parser.add_argument('confirmPassword', required=True, help="confirmPassword is required.")
        data = parser.parse_args()
        try:
            user = UserRepository(username=data['username'],
                            email=data['email'],
                            password=data['password'])
            print('data', data)
            user.check_confirm_password(data['password'], data['confirmPassword'])
            user.hash_password()
            user.save()
            user.save_session()
            id = str(user.id)
            message = "registration success"

            return {"msg": message, "id": id}, 200

        except Exception as e:
            return {"errors": abort_msg(e)}, 500


class LoginApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", required=True, help='account is required')
        parser.add_argument("password", required=True, help='password is required')
        data = parser.parse_args()

        try:
            query = UserRepository.get_user(data['email'])
            if query != None and query.verify_password(data['password']):
                query.save_session()
                return {'msg': "ok", "id": str(query.id)}, 200
            else:
                return {'msg': 'incorrect email or password error'}, 400
        except Exception as e:
            return {'errors': abort_msg(e)}, 500


class LogoutApi(Resource):
    def post(self):
        UserRepository.remove_session()


def init_auth(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(LogoutApi, '/api/auth/logout')
