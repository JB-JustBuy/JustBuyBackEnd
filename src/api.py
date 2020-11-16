from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from src.resources.user_controller import UserController
from src.resources.search_merchandise_controller import SearchMerchandiseController
class DevConfig(object):
    DEBUG = True


app = Flask("just_buy")
api = Api(app)
app.config.from_object(DevConfig)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    data = request.get_json()
    print(data)
    return data if data != None else {"status": "error"}


api.add_resource(SearchMerchandiseController, "/search")
api.add_resource(UserController, '/user/')

if __name__ == "__main__":
    app.run()