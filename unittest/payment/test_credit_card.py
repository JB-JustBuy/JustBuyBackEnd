import unittest
from src.utilities.payment.credit_card import CreditCard
from src.utilities.merchandise.merchandise import Merchandise


class TestCreditCard(unittest.TestCase):
    def setUp(self):
        self.credit_card = CreditCard("test", "玉山銀行")

    def test_is_merchandise_conform_qualifications(self):
        md1 = Merchandise("test01", 1000, "shoppe", "url001")
        md2 = Merchandise("test02", 1000, "pchome", "url002")

        self.credit_card.qualify(md)


