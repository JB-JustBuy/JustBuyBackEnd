from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.entities.payment.credit_card import CreditCard
from src.entities.discount_config import config
from src.entities.scraper.pchome_data_controller import PChomeDataController
from src.entities.scraper.shoppe_data_controller import ShoppeDataController
from src.entities.merchandise.merchandise import Merchandise
from src.entities.payment.payment import Payment
import numpy as np
import json
class DiscountModel:
    def __init__(self, model_config):
        self.payments = list()
        self.__set_config(model_config)

    def calculate(self, merchandises: dict) -> (Payment, int):
        merchandises_list = merchandises.values()
        feedback = []
        for payment in self.payments:
            best_method = payment.get_qualified_best_method(merchandises_list)
            feedback.append(best_method.feedback())
        max_feedback_idx = np.argmax(feedback)
        return self.payments[max_feedback_idx], feedback[max_feedback_idx]

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
                    raise  ValueError('feedback config error')
                payment.add_method(FeedBackMethod(constraint, feedback))

            if payment != None:
                self.payments.append(payment)

    def get_config(self):
        return json.dumps({
            'payments': [payment.to_dict() for payment in self.payments],
        }, indent=1)


if __name__ == '__main__':
    keyword = input("Please input the product name and mode:")
    keyword = '羅技g604'
    # pchome = PChomeDataController()
    # pchome.search([keyword])
    # pchome_products = pchome.result

    shoppe = ShoppeDataController()
    shoppe.search([keyword])
    shoppe_products = shoppe.result
    #
    merchandises = Merchandise.generate_merchandises(shoppe_products)
    shoppe_merchandises = Merchandise.find_the_cheapest(merchandises)
    print("shoppe_merchandises: ", shoppe_merchandises)
    print("The cheapest merchandise(pick from shoppe):")
    for key, item in shoppe_merchandises.items():
        print("Keyword:{}\n".format(key))
        print(item.to_dict())

    print()

    # merchandises = Merchandise.generate_merchandises(pchome_products)
    # pchome_merchandises = Merchandise.find_the_cheapest(merchandises)
    # print("pchome_merchandises: ", pchome_merchandises)
    # print('The cheapest merchandise(pick from pchome):')
    # for key, item in pchome_merchandises.items():
    #     print("Keyword:{}".format(key))
    #     print(item.to_dict())

    # init model
    model = DiscountModel(config)
    # print(model.get_config())
    payment, feedback = model.calculate(shoppe_merchandises)
    print("shoppe best payment:", payment.to_dict())
    print('feedback:', feedback)

    # payment, feedback = model.calculate(pchome_merchandises)
    # print("pchome best payment:", payment.to_dict())
    # print('feedback:', feedback)
