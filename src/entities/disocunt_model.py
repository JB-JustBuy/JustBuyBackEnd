from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.entities.merchandise import select_merchdise_strategy
from src.entities.payment.credit_card import CreditCard
from src.entities.discount_config import config
from src.entities.merchandise.merchandise import Merchandise
from src.entities.payment.payment import Payment
import numpy as np
import json


class DiscountModel:
    def __init__(self, scrapy_model, discount_config):
        self.payments = list()
        self.scrapy_model = scrapy_model
        self.__set_config(discount_config)
        self.select_merchandise_strategy = select_merchdise_strategy.CheapestStrategy()

    def calculate(self, merchandises: dict) -> (Payment, int):
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

    def handle_select_merchandise_strategy(self, merchandises):
        selected = {}
        for name, searched_merchandises in merchandises.items():
            selected[name] = self.select_merchandise_strategy.find_ideal(searched_merchandises)
        return selected

    def process_one_platform_search_result(self, platform: str):
        merchandises = self.__get_merchandise_from_scrapy_model(platform)
        merchandises = self.handle_select_merchandise_strategy(merchandises)
        payment, feedback = self.calculate(merchandises)
        return payment, feedback


    def __get_merchandise_from_scrapy_model(self, platform):
        for key, data in self.scrapy_model.scrapies.items():
            if key == platform:
                merchandises = Merchandise.from_dict(data['scrapy'].result)
                return merchandises

        raise ValueError('Cant find the search result in {} platform'.format(platform))

    def __set_config(self, model_config):
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

    def get_config(self):
        return json.dumps({
            'payments': [payment.to_dict() for payment in self.payments],
        }, indent=1)


if __name__ == '__main__':
    import logging
    from src.entities.scrapy_model import ScrapyModel


    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='w', format=FORMAT)

    keyword = input("Please input the product name and mode:")
    keyword = '羅技g604'

    scrapy_model = ScrapyModel.generate_scrapy_model(platforms='all')
    scrapy_model.search([keyword], scrapy_key='all')


    # init model
    model = DiscountModel(scrapy_model, config)
    payment, feedback = model.process_one_platform_search_result(platform='pchome')


