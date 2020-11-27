from src.entities.feedback_constraint.quantity_enough import QuantityEnough
from src.entities.merchandise.merchandise import Merchandise
import unittest


class TestSingleFull(unittest.TestCase):
    def setUp(self):
        self.constraint = QuantityEnough(5, "pchome", "3C")

    def test_qualify(self):
        merchandises = [Merchandise("test001", 300, "shoppe", "test_url_001", quantity=5)]
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test002", 1000, "pchome", "test_url_002", quantity=3))
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test003", 1500, "pchome", "test_url_003", md_type="food", quantity=5))
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test003", 1500, "pchome", "test_url_003", md_type="3C", quantity=5))
        self.assertTrue(self.constraint.qualify(merchandises))