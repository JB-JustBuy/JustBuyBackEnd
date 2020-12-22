from src.utilies.parser.price_parser import PriceParser
import numpy as np
import re

class Merchandise(object):
    def __init__(self, name, price, platform, url, md_type=None, quantity=1):
        self.name = name
        self.price = PriceParser.price_parser(price)
        self.platform = platform
        self.url = url
        self.md_type = md_type
        if quantity >= 1:
            self.quantity = quantity
        else:
            raise Exception("Merchandise Quantity need to bigger than 0.")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "platform": self.platform,
            'url': self.url,
            "md_type": self.md_type
        }



    @staticmethod
    def from_dict(md_dict: dict):
        name = md_dict['name'] if 'name' in md_dict else None
        price = md_dict['price'] if 'price' in md_dict else None
        platform = md_dict['platform'] if 'platform' in md_dict else None
        url = md_dict['url'] if 'url' in md_dict else None
        return Merchandise(name, price, platform, url)

    @staticmethod
    def from_searching_engine_scrapy_result(scrape_result: dict) -> dict:
        merchandises = []
        products = {}
        for product_name, search_result in scrape_result.items():
            for item in search_result:
                print(item)
                name = item["name"]
                price = item['price']
                platform = item['platform']
                url = item['url']
                md_type = None
                if "type" in item.keys():
                    md_type = item[md_type]
                merchandises.append(Merchandise(name, price, platform, url, md_type))
            products[product_name] = merchandises
            merchandises = []
        return products

    @staticmethod
    def find_the_cheapest(merchandises: dict) -> dict:
        result = {}
        for name, items in merchandises.items():
            cheapest_idx = np.argmin([int(item.price) for item in items])
            result[name] = items[cheapest_idx]
        return result
