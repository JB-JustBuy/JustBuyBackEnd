from src.utilities.feedback_constraint.single_full import SingleFull
from src.utilities.merchandise.merchandise import Merchandise
import unittest


class TestSingleFull(unittest.TestCase):
    def setUp(self):
        self.constraint = SingleFull(1500, "pchome")

    def test_qualify(self):
        merchandises = [Merchandise("test001", 300, "shoppe", "test_url_001")]
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test002", 1000, "pchome", "test_url_002"))
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test003", 1500, "shoppe", "test_url_003"))
        self.assertFalse(self.constraint.qualify(merchandises))

        merchandises.append(Merchandise("test003", 1500, "pchome", "test_url_003"))
        self.assertTrue(self.constraint.qualify(merchandises))
