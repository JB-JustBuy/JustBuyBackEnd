import unittest
from src.entities.payment.payment import Payment
from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.entities.merchandise.merchandise import Merchandise

class TestPayment(unittest.TestCase):
    def setUp(self):
        self.payment = Payment()
        self.method1 = FeedBackMethod(
            SingleFull(amount=1000),
            Cash(amount=100),
        )
        self.method2 = FeedBackMethod(
            SingleFull(amount=1500),
            Cash(amount=100),
        )
        self.method3 = FeedBackMethod(
            SingleFull(amount=1000,  platform="shoppe"),
            Cash(amount=150),
        )
        self.md1 = Merchandise("test001", 1000, "pchome", "url001")
        self.md2 = Merchandise("test002", 1000, "shoppe", "url002")

    def test_add_method(self):
        error_type = 1000
        try:
            self.payment.add_method(error_type)
        except TypeError:
            self.assertTrue(TypeError)

        method = FeedBackMethod(SingleFull(amount=1000),
                                Cash(amount=100))
        self.payment.add_method(method)
        self.assertEqual(1, len(self.payment.methods))

    def test_get_best_method(self):
        self.payment.add_method(self.method1)
        self.payment.add_method(self.method2)
        self.payment.add_method(self.method3)

        best = self.payment.get_best_method(self.payment.methods)
        self.assertEqual(self.method3, best)

    def test_get_qualified_best_method(self):

        self.payment.add_method(self.method1)
        self.payment.add_method(self.method2)
        self.payment.add_method(self.method3)

        # best = self.payment.get_qualified_best_method([self.md1], self.payment.methods)
        # self.assertEqual(best.constraint, self.method1.constraint)

        best = self.payment.get_qualified_best_method([self.md2], self.payment.methods)
        self.assertEqual(best.constraint, self.method3.constraint)