from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.generator.filter_strategy_generator import FilterStrategyGenerator
from src.entities.payment.credit_card import CreditCard
from src.entities.discount_config import config
from src.entities.merchandise.merchandise import Merchandise
from itertools import product
from src.entities.payment.payment import Payment
import numpy as np
import json, os


class DiscountModel:
    def __init__(self, scrapy_model, discount_config=config, strategy_type='familiar'):
        self.payments = list()
        self.scrapy_model = scrapy_model
        self.__set_config(discount_config)
        self.strategy_type = strategy_type

    # def calculate(self, merchandises: dict) -> (Payment, int):
    #     merchandises_list = merchandises.values()
    #     feedback = []
    #     try:
    #         for payment in self.payments:
    #             best_method = payment.get_qualified_best_method(merchandises_list)
    #             if best_method != []:
    #                 feedback.append(best_method.feedback())
    #         max_feedback_idx = np.argmax(feedback)
    #         return self.payments[max_feedback_idx], feedback[max_feedback_idx]
    #     except ValueError as e:
    #         print(e)
    #     except Exception as e:
    #         print(e)
    #
    # def handle_select_merchandise_by_strategy(self, merchandises):
    #     selected = {}
    #     for name, searched_merchandises in merchandises.items():
    #         self.select_merchandise_strategy = self._get_strategy(searched_merchandises)
    #         selected[name] = self.select_merchandise_strategy.find_ideal(searched_merchandises)
    #     return selected
    #
    # def find_best_discount_from_one_paltform_scrapy_result(self, platform: str):
    #     merchandises = self.__get_merchandise_from_scrapy_model(platform)
    #     merchandises = self.handle_select_merchandise_by_strategy(merchandises)
    #     payment, feedback = self.calculate(merchandises)
    #     return payment, feedback

    def analysis(self):
        acceptable_mds = self.get_products_acceptable_merchandises()
        # combinations = self.__get_permutations(acceptable_mds)
        return acceptable_mds

    def get_products_acceptable_merchandises(self) -> dict:
        products_acceptable_md = {}
        product_names = self.scrapy_model.keywords
        ref_mds = self.scrapy_model.md_by_url
        for product_name, (url, md_dict) in zip(product_names, ref_mds.items()):
            search_items = self.__get_merchandise_from_scrapy_model_by_product_name(product_name)
            ref_md = Merchandise.from_dict(md_dict)
            acceptable_items = self.__filter_product_by_strategy(search_items, ref_md)
            products_acceptable_md.update({product_name: acceptable_items})
            print('searched item: {}, acceptable items: {}'.format(len(search_items),
                                                                   len(acceptable_items)))
        return products_acceptable_md

    def get_config(self):
        return json.dumps({
            'payments': [payment.to_dict() for payment in self.payments],
        }, indent=1)

    def __get_permutations(self, merchandises: dict):
        return [dict(zip(merchandises, v)) for v in product(*merchandises.values())]

    def __get_merchandise_from_scrapy_model_by_platform(self, platform: str):
        for key, data in self.scrapy_model.scrapies.items():
            if key == platform:
                merchandises = Merchandise.from_searching_engine_scrapy_result(data['scrapy'].result)
                with open(os.path.join('.', 'search result{}.txt'.format(platform)), 'w') as file:
                    file.write(json.dumps(data['scrapy'].result, indent=1))
                return merchandises
        raise ValueError('Cant find the search result in {} platform'.format(platform))

    def __get_merchandise_from_scrapy_model_by_product_name(self, product_name: str):
        products = []
        for platform, platform_scrapies in self.scrapy_model.scrapies.items():
            merchandises = Merchandise.from_searching_engine_scrapy_result(platform_scrapies['engine_scrapy'].result)
            products += merchandises[product_name]
        return products

    def __set_config(self, model_config: dict):
        for name, config in model_config.items():
            type = config['type']
            belong = config['belong']
            if type == 'CreditCard' or type == '信用卡' or type == 'credit card':
                payment = CreditCard(name, belong)
            else:
                raise ValueError("payment config error")

            for method in config['methods']:
                if method['constraint']['type'] == '單筆':
                    constraint = SingleFull(int(method['constraint']['value']))
                else:
                    raise ValueError('constraint config error')
                if method['feedback']['type'] == '現金':
                    feedback = Cash(int(method['feedback']['value']))
                else:
                    raise ValueError('feedback config error')
                payment.add_method(FeedBackMethod(constraint, feedback))

            if payment != None:
                self.payments.append(payment)

    def __filter_product_by_strategy(self, search_items: list, ref_md: Merchandise) -> list:

        """
        :input: [md1_001, md1_002, md1_003, md1_004, md1_005, md1_006]
        :return: [md1_001, md1_002, md1_003],
        """

        filter_merchandise_strategy = FilterStrategyGenerator.generate_strategy(self.strategy_type, ref_md)

        return filter_merchandise_strategy.filter(search_items)


if __name__ == '__main__':
    import logging
    from src.entities.scrapy_model import ScrapyModel

    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='w', format=FORMAT)

    urls = ['https://shopee.tw/%E3%80%90%E5%85%A8%E6%96%B0%E3%80%91-PS4-Slim-500GB-1TB-%E7%99%BD-%E9%BB%91-%E4%B8%BB%E6%A9%9F-%E5%8F%B0%E7%81%A3%E5%85%AC%E5%8F%B8%E8%B2%A8-CUH-2218A-%E5%8F%AF%E9%9D%A2%E4%BA%A4-Pro-%E9%AD%94%E7%89%A9%E7%8D%B5%E4%BA%BA-i.14159223.1326072367']

    scrapy_model = ScrapyModel.generate_scrapy_model(platforms='all')
    scrapy_model.search(urls)

    # init model
    model = DiscountModel(scrapy_model, strategy_type='familiar')
    products_acceptable_items = model.analysis()
    print(products_acceptable_items)
