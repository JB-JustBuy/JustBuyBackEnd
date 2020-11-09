from flask import Flask, request
from flask_cors import CORS

class DevConfig(object):
    DEBUG = True

app = Flask("just_buy")
app.config.from_object(DevConfig)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    data = request.get_json()
    print(data)
    return data if data != None else {"status": "error"}

@app.route("/search")
def search():
    data = request.args
    print(data)
    return data if data != None else {"status": "error"}

if __name__ == "__main__":
    app.run()