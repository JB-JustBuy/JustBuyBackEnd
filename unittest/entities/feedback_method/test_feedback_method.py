import unittest
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.merchandise.merchandise import Merchandise


class TestFeedBackMethod(unittest.TestCase):
    def setUp(self):
        constraint = SingleFull(1000, "shoppe")
        form = Cash(amount=100)
        self.method = FeedBackMethod(constraint, form)

    def test_trigger(self):
        merchandises = [Merchandise("test001", 300, "shoppe", "test_url_001")]
        self.assertFalse(self.method.qualify(merchandises))

        merchandises.append(Merchandise("test002", 1000, "pchome", "test_url_002"))
        self.assertFalse(self.method.qualify(merchandises))

        merchandises.append(Merchandise("test003", 1000, "shoppe", "test_url_003"))
        self.assertEqual(100, self.method.trigger(merchandises))

    def test_integration(self):
        from src.entities.scrapy.pchome_searching_engine_scrapy import PChomeSearchingEngineScrapy
        from src.entities.scrapy.shoppe_searching_engine_scrapy import ShoppeSearchingEngineScrapy
        from src.entities.merchandise.merchandise import Merchandise
        from src.entities.feedback_method.feedback_method import FeedBackMethod
        from src.entities.feedback_constraint.single_full import SingleFull
        from src.entities.feedback_form.cash import Cash

        keyword = input("Please input the product name and mode:")

        pchome = PChomeSearchingEngineScrapy()
        pchome.search(keyword)
        pchome_products = pchome.products

        shoppe = ShoppeSearchingEngineScrapy()
        shoppe.search(keyword)
        shoppe_products = shoppe.products

        merchandises = Merchandise.generate_merchandises(shoppe_products)
        shoppe_merchandise = Merchandise.find_the_cheapest(merchandises)
        print("The cheapest merchandise(pick from shoppe):\n  name:{}\n   price:{}\n  platform:{}\n url:{}".format(
            shoppe_merchandise.name,
            shoppe_merchandise.price,
            shoppe_merchandise.platform,
            shoppe_merchandise.url
        ))

        merchandises = Merchandise.generate_merchandises(pchome_products)
        pchome_merchandise = Merchandise.find_the_cheapest(merchandises)
        print("The cheapest merchandise(pick from pchome):\n  name:{}\n   price:{}\n  platform:{}\n url:{}".format(
            pchome_merchandise.name,
            pchome_merchandise.price,
            pchome_merchandise.platform,
            pchome_merchandise.url
        ))

        form1 = Cash(amount=100)
        form2 = Cash(pct=0.03)
        constraint1 = SingleFull(amount=1000)
        constraint2 = SingleFull(amount=900, platform='shoppe')
        method1 = FeedBackMethod(constraint1, form1)
        method2 = FeedBackMethod(constraint2, form2)


        print("Shoppe Merchandise in Method(001) feedback:", method1.feedback([shoppe_merchandise]))
        self.assertEqual(100, method1.feedback([shoppe_merchandise]))
        # 這個怪怪的 單筆超過900回饋0.03, 但目前僅以900*0.03計算=27, 未考慮(超過部分）
        print("Shoppe Merchandise in Method(002) feedback:", method2.feedback([shoppe_merchandise]))
        self.assertEqual(27, method2.feedback([shoppe_merchandise]))

        print("PChome Merchandise in Method(001) feedback:", method1.feedback([pchome_merchandise]))
        # 這個怪怪的 單筆超過900回饋0.03, 但目前僅以900*0.03計算=27, 未考慮(超過部分
        self.assertEqual(100, method1.feedback([pchome_merchandise]))
        print("PChome Merchandise in Method(002) feedback:", method2.feedback([pchome_merchandise]))
        self.assertEqual(100, method1.feedback([pchome_merchandise]))
