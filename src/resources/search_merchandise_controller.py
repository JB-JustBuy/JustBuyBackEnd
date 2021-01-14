from flask_login import login_required
from flask_restful import Resource, request, reqparse
from src.resources.auth import login_required
from src.entities.scrapy_model import ScrapyModel
from src.entities.disocunt_model import DiscountModel
import json


# class SearchMerchandiseController(Resource):
#     @login_required()
#     def get(self):
#         key_words = request.args.get("keyword").split(' ')
#         driver = ShoppeSearchingEngineScrapy.get_driver()
#         scraper = ShoppeSearchingEngineScrapy(driver)
#         scraper.search(key_words)
#         result = json.dumps(scraper.result, indent=1)
#         return result,  200


class SearchByUrlController(Resource):
    # @login_required()
    def post(self):
        # process font end paras
        rp = reqparse.RequestParser()
        rp.add_argument('urls', required=True, action='append', help='Urls is required')
        args = rp.parse_args()
        # call scrapy to search the same product
        scrapy_model = ScrapyModel.generate_scrapy_model('all')
        scrapy_model.search(args['urls'])

        # call discount analysis to find best return method
        discount_model = DiscountModel(scrapy_model)
        feed_back = discount_model.analysis()
        return feed_back
