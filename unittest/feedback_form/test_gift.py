from src.feedback_form.gift import Gift
from src.merchandise.merchandise import Merchandise
import unittest


class TestGift(unittest.TestCase):
    def setUp(self):
        self.gift_1 = Gift(Merchandise("test1", 100, "pchome", "url_test", md_type="3C", quantity=1))
        self.gift_2 = Gift(Merchandise("test1", 100, "pchome", "url_test", md_type="3C", quantity=10))

    def test_paras_type(self):
        try:
            gift = Gift(10)
        except TypeError:
            self.assertTrue(TypeError)

    def test_feedback(self):
        self.assertEqual(100, self.gift_1.feedback())
        self.assertEqual(1000, self.gift_2.feedback())

