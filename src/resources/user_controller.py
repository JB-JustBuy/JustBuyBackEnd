from flask_restful import Resource
from src.repository.user_repository import UserRepository


class UserController(Resource):
    def get(self,):
        data = {
            "database": "just_buy",
            "collection": "users"
        }
        user_api = UserRepository(data)
        users = user_api.read()
        return {
            "message": "success",
            "users": users
        }, 200

