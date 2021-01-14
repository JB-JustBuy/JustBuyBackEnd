from flask import Flask, request
from flask_session import Session
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from src.repository.db import initialize_db
from src.resources.search_merchandise_controller import SearchByUrlController
from src.resources.auth import init_auth
from src.resources.user import init_user

class DevConfig(object):
    DEBUG = True
    SESSION_TYPE = 'mongodb'
    SECRET_KEY = 'fooledbyrandomness'
    SESSION_KEY_PREFIX = 'session'
    PERMANENT_SESSION_LIFETIME = 600
    MONGODB_SETTINGS = {
        'host': "mongodb://localhost:27017/just_buy"
    }


app = Flask("just_buy")
app.config.from_object(DevConfig)
initialize_db(app)
bcrypt = Bcrypt(app)
Session(app)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)
api = Api(app)


@app.route('/', methods=['GET'])
def index():
    data = request.json
    return data if data != None else {"status": "error"}

api.add_resource(SearchByUrlController, "/api/search")

init_auth(api)
init_user(api)
if __name__ == "__main__":
    app.run(debug=True)
