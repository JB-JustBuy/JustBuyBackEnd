from flask_restful import Resource
from flask import session, jsonify


class Profile(Resource):
    def get(self):
        if session.get('id') != None:
            username = str(session.get('username'))
            email = str(session.get('email'))
            print("username", username, 'email', email)
            return {"username": username,
                    'email': email}, 200
        else:
            return {"msg": "require login"}, 400


def init_user(app):
    app.add_resource(Profile, '/api/user/profile')
