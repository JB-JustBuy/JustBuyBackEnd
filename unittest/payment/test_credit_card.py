import unittest
from src.payment.credit_card import CreditCard
from src.feedback_method.feedback_method import FeedBackMethod
from src.feedback_constraint.single_full import SingleFull
from src.feedback_form.cash import Cash
from src.merchandise.merchandise import Merchandise


class TestCreditCard(unittest.TestCase):
    def setUp(self):
        self.credit_card = CreditCard("test", "玉山銀行")

    def test_is_merchandise_conform_qualifications(self):
        md1 = Merchandise("test01", 1000, "shoppe", "url001")
        md2 = Merchandise("test02", 1000, "pchome", "url002")

        self.credit_card.qualify(md)


