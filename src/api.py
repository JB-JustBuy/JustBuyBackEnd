from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from src.repository.db import initialize_db
from src.resources.search_merchandise_controller import SearchMerchandiseController
from src.resources.auth import init_auth


class DevConfig(object):
    DEBUG = True
    SECRET_KEY = '2xa93f2D3mdA'
    SESSION_TYPE = 'redius'
    MONGODB_SETTINGS = {
        'host': "mongodb://localhost:27017/just_buy"
    }


app = Flask("just_buy")
app.config.from_object(DevConfig)
initialize_db(app)
bcrypt = Bcrypt(app)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)
api = Api(app)


@app.route('/', methods=['GET'])
def index():
    data = request.json
    return data if data != None else {"status": "error"}

# @app.route('/normal_member')
# @check_login('normal')
# def member_normal_page():
#     return 'ok'

api.add_resource(SearchMerchandiseController, "/search")
init_auth(api)
if __name__ == "__main__":
    app.run()
