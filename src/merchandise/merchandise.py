import numpy as np
class Merchandise(object):
    def __init__(self, name, price, platform, url, md_type=None):
        self.name = name
        self.price = price
        self.platform = platform
        self.url = url
        self.md_type = md_type

    @staticmethod
    def generate_merchandises(products):
        merchandises = []
        for product in products:
            name = product["name"]
            price = product['price']
            platform = product['platform']
            url = product['url']
            md_type = None
            if "type" in product.keys():
                md_type = product[md_type]
            merchandises.append(Merchandise(name, price, platform, url, md_type))

    @staticmethod
    def find_the_cheapest(merchandises):
        cheapest_idx = np.argmin([merchandise.price for merchandise in merchandises])
        return merchandises[cheapest_idx]
