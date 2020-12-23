from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.generator.filter_strategy_generator import FilterStrategyGenerator
from src.generator.payment_generator import PaymentGenerator
from src.generator.constraint_generator import ConstraintGenerator
from src.generator.feedback_generator import FeedBackGenerator
from src.entities.discount_config import config
from src.entities.merchandise.merchandise import Merchandise
from src.entities.payment.payment import Payment
from itertools import product
import numpy as np
import json, os


class DiscountModel:
    def __init__(self, scrapy_model, discount_config=config, strategy_type='familiar'):
        self.payments = list()
        self.scrapy_model = scrapy_model
        self.__set_config(discount_config)
        self.strategy_type = strategy_type
        self.product_candidate_limit = 5

    def analysis(self):
        acceptable_mds = self.get_products_acceptable_merchandises()
        product_permutations = self.__get_permutations(acceptable_mds)
        payment_feedback = self.get_permutations_feedback(product_permutations)
        return payment_feedback

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
    def get_permutations_feedback(self, permutations: list):
        """

        :param permutations: [permutation1, permutation2, permutation3...]
        :return: [[payment1, feedback1], [payment2, feedback2], ...]
        """
        payment_and_feedback = []
        for permutation in permutations:
            payment, feedback = self.calculate_feedback(permutation)
            payment_and_feedback.append([payment, feedback])
            print(payment, feedback)

        return payment_and_feedback

    def get_products_acceptable_merchandises(self) -> dict:
        products_acceptable_md = {}
        product_names = self.scrapy_model.keywords
        ref_mds = self.scrapy_model.md_by_url

        for product_name, (url, md_dict) in zip(product_names, ref_mds.items()):

            search_items = self.__get_merchandise_from_scrapy_model_by_product_name(product_name)
            ref_md = Merchandise.from_dict(md_dict)
            # data is from url have
            if not ref_md.is_complete():
                raise Exception('Cant get acceptable merchandise because reference merchandise is not complete')
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
            payment = PaymentGenerator.generate_payment(type, name=name, belong=belong)

            for method in config['methods']:
                # set constraint
                constraint_type = method['constrain']['type']
                value = method['constrain']['value']

                constraint = ConstraintGenerator.generate_constraint(constraint_type, value=value)

                # set feedback
                feedback_type = method['feedback']['type']
                value = method['feedback']['value']
                feedback = FeedBackGenerator.generate_feedback(feedback_type, value=value)

                # add to payment
                payment.add_method(FeedBackMethod(constraint, feedback))

            if payment != None:
                self.payments.append(payment)

    def calculate_feedback(self, merchandises: dict) -> (Payment, int):
        merchandises_list = merchandises.values()
        feedback = []
        try:
            for payment in self.payments:
                best_method = payment.get_qualified_best_method(merchandises_list)
                if best_method != []:
                    feedback.append(best_method.feedback())
            max_feedback_idx = np.argmax(feedback)
            return self.payments[max_feedback_idx], feedback[max_feedback_idx]
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

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

    urls = ["https://24h.pchome.com.tw/prod/DGBJA7-1900B1QBE",
            'https://24h.pchome.com.tw/prod/DYAN3U-A900B1KWU']
    scrapy_model = ScrapyModel.generate_scrapy_model(platforms='all')
    scrapy_model.search(urls)

    # init model
    model = DiscountModel(scrapy_model, strategy_type='familiar')
    products_acceptable_items = model.analysis()
    print(products_acceptable_items)
