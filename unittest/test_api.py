import unittest
from flask import Flask
from flask_restful import Api, Resource
from flask_restful.utils import cors
from flask_cors import CORS

class TestCORSCase(unittest.TestCase):
    def test_crossdomain(self):
        app = Flask(__name__)
        api = Api(app)

        class Foo(Resource):
            def get(self):
                return "data"
        api.add_resource(Foo, '/')
        CORS(app)

        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.headers['Access-Control-Allow-Origin'], "*")


