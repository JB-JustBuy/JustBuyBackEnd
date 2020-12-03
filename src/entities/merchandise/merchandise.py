import numpy as np


class Merchandise(object):
    def __init__(self, name, price, platform, url, md_type=None, quantity=1):
        self.name = name
        self.price = price
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
    def generate_merchandises(scrape_result: dict) -> dict:
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
