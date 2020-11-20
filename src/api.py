from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from src.resources.sign_up import SignUpController
from src.resources.search_merchandise_controller import SearchMerchandiseController


class DevConfig(object):
    DEBUG = True


app = Flask("just_buy")
app.config.from_object(DevConfig)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)
api = Api(app)


@app.route('/', methods=['GET'])
def index():
    data = request.get_json()
    print(data)
    return data if data != None else {"status": "error"}


api.add_resource(SearchMerchandiseController, "/search")
api.add_resource(SignUpController, '/signup/')

if __name__ == "__main__":
    app.run()
