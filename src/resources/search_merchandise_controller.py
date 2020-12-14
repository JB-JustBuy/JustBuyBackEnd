from flask_login import login_required
from flask_restful import Resource, request
from src.resources.auth import login_required
from src.entities.scrapy.shoppe_scrapy import ShoppeScrapy
import json


class SearchMerchandiseController(Resource):
    @login_required()
    def get(self):
        key_words = request.args.get("keyword").split(' ')
        scraper = ShoppeScrapy()
        scraper.search(key_words)
        result = json.dumps(scraper.result, indent=1)
        return result,  200
