import unittest
from src.feedback_constraint.single_full import SingleFull
from src.feedback_form.cash import Cash
from src.feedback_method.feedback_method import FeedBackMethod
from src.merchandise.merchandise import Merchandise


class TestFeedBackMethod(unittest.TestCase):
    def setUp(self):
        constraint = SingleFull(1000, "shoppe")
        form = Cash(amount=100)
        self.method = FeedBackMethod(constraint, form)

    def test_trigger(self):
        merchandises = [Merchandise("test001", 300, "shoppe", "test_url_001")]
        self.assertFalse(self.method.is_satisfied(merchandises))

        merchandises.append(Merchandise("test002", 1000, "pchome", "test_url_002"))
        self.assertFalse(self.method.is_satisfied(merchandises))

        merchandises.append(Merchandise("test003", 1000, "shoppe", "test_url_003"))
        self.assertEqual(100, self.method.trigger(merchandises))