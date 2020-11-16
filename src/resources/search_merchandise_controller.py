from flask_restful import Resource, request, ResponseBase
from src.utilities.scraper.shoppe_data_controller import ShoppeDataController
import json


class SearchMerchandiseController(Resource):
    def get(self):
        key_words = request.args.get("keyword").split(' ')
        scraper = ShoppeDataController()
        scraper.search(key_words)
        result = json.dumps(scraper.result, indent=1)
        return result,  200