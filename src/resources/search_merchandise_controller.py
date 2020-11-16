from flask_restful import Resource, request
from src.utilities.scraper.shoppe_data_controller import ShoppeDataController


class SearchMerchandiseController(Resource):
    def get(self):
        key_words = request.args.get("key_word").split(' ')
        scraper = ShoppeDataController()
        scraper.search(key_words)
        result = scraper.result
        return {
            "message": "",
            "key_words": key_words,
            "result": result
        },  200