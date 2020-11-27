from flask import session, jsonify, make_response
from flask_restful import Resource, reqparse, abort
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
    def get(self):
        id = session.get("id")
        username = session.get('username')
        email = session.get('email')
        return make_response(jsonify(id=id,
                                     username=username,
                                     email=email), 200)


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


def login_required():
    def decorator(func):
        def wrap(*args, **kw):
            user_id = session.get('id')
            if user_id == None or user_id == '':
                return abort(401)
            else:
                return func(*args, **kw)

        wrap.__name__ = func.__name__
        return wrap

    return decorator

def init_auth(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(LogoutApi, '/api/auth/logout')
