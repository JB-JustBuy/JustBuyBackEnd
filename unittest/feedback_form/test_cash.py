from src.utilities.feedback_form.cash import Cash
import unittest


class TestCash(unittest.TestCase):
    def setUp(self):
        self.form_amount = Cash(amount=100)
        self.form_pct = Cash(pct=0.03)
        self.form_mix = Cash(amount=100, pct=0.01)

    def test_feedback(self):
        price = 1000
        self.assertEqual(100, self.form_amount.feedback(price))
        self.assertEqual(30, self.form_pct.feedback(price))
        self.assertEqual(110, self.form_mix.feedback(price))
