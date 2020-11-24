from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_login import LoginManager
from src.resources.sign_up import SignUpController
from src.resources.search_merchandise_controller import SearchMerchandiseController
from src.resources.login import Login
from src.repository.config import USER_REPOSITORY_CONFIG
from src.entities.user.user import User

class DevConfig(object):
    DEBUG = True
    SECRET_KEY = '2xa93f2D3mdA'

app = Flask("just_buy")
app.config.from_object(DevConfig)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


login_manager = LoginManager(app)
@login_manager.user_loader
def user_loader(email):
    return User.get(email)


api = Api(app)


@app.route('/', methods=['GET'])
def index():
    data = request.get_json()
    return data if data != None else {"status": "error"}


api.add_resource(SearchMerchandiseController, "/search")
api.add_resource(SignUpController, '/signup/',
                 resource_class_kwargs={
                    "repository": USER_REPOSITORY_CONFIG
                 })

api.add_resource(Login, '/login/',
                 resource_class_kwargs={
                    'repository': USER_REPOSITORY_CONFIG
                })
if __name__ == "__main__":
    app.run()
