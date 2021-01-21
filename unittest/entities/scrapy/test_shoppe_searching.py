import unittest
from src.entities.scrapy.shoppe_searching_engine_scrapy import ShoppeSearchingEngineScrapy


class TestShoppeSearchingEngine(unittest.TestCase):
    def setUp(self):
        self.scrapy = ShoppeSearchingEngineScrapy()

    def test_simple_run(self):
        keywords = ['魔物獵人']
        result = self.scrapy.search(keywords)



