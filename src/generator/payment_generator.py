from src.entities.payment.credit_card import CreditCard


class PaymentGenerator:
    @staticmethod
    def generate_payment(payment_type, **kwargs):
        if payment_type == 'CreditCard' or payment_type == '信用卡' or payment_type == 'credit card':
            if "name" not in kwargs or 'belong' not in kwargs:
                raise KeyError("Payement require 'name' and 'belong' paras")
            else:
                return CreditCard(kwargs['name'], kwargs['belong'])
        else:
            raise ValueError("payment config error")
