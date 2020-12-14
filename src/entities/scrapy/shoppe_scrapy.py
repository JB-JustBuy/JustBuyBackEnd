from src.entities.scrapy.scrapy import Scrapy
import os


class ShoppeScrapy(Scrapy):
    def __init__(self, driver_path=None):
        super().__init__()
        self.url = "https://shopee.tw/search?keyword="
        self.driver = self.get_driver()
        self.platform = "shoppe"

    def parser(self):
        elem_row = self.driver.find_element_by_xpath("//div[@class='row shopee-search-item-result__items']")
        elem_names = elem_row.find_elements_by_xpath('//div[@class="_1NoI8_ _16BAGk"]')
        elem_ads = elem_row.find_elements_by_xpath('//div[@data-sqe="ad"]')
        elem_links = elem_row.find_elements_by_xpath('//a[@data-sqe="link"]')
        elem_prices = elem_row.find_elements_by_xpath('//*[@class="_341bF0"]')

        products = []
        for index, (name, link, price) in enumerate(zip(elem_names, elem_links, elem_prices)):
            print("Index:", index)
            print(' name:{}, platform:{}, price:{}\n link:{}\n'.format(name.get_attribute("innerHTML").splitlines()[0],
                                                                    self.platform,
                                                                    price.get_attribute("innerHTML").splitlines()[0],
                                                                    link.get_attribute("href")))
            if index >= len(elem_ads):
                product = {
                    "name": name.get_attribute("innerHTML").splitlines()[0],
                    "price":  int(price.get_attribute("innerHTML").splitlines()[0].replace(',', "")),
                    "url": link.get_attribute("href"),
                    "platform": self.platform
                }
                products.append(product)
        return products


if __name__ == '__main__':
    import json
    dc = ShoppeScrapy()
    dc.search(['羅技G604'])
    print(json.dumps(dc.result, indent=1))
