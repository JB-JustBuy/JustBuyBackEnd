from src.entities.scrapy.searching_merchandise_page_scrapy import MerchandisePageScrapy
import time


class ShoppeMerchandisePageScrapy(MerchandisePageScrapy):
    def __init__(self):
        super().__init__()
        self.PLATFORM = 'shoppe'

    def parse(self, url):
        self.driver.get(url)

        name = self._get_name()
        original_price = self._get_original_price()
        sale_price = self._get_sale_price()

        if sale_price is not None:
            price = sale_price
        elif original_price is not None:
            price = original_price
        else:
            price = None

        md = {
            'name': name,
            'price': price,
            'platform': self.PLATFORM,
            'url': url
        }
        return md

    def _get_name(self):
        NAME_ClASS = 'qaNIZv'
        self._wait(NAME_ClASS)
        xpath = "//div[@class='{}']".format(NAME_ClASS)
        name_div = self.driver.find_element_by_xpath(xpath)
        name = name_div.find_element_by_xpath('span').get_attribute('innerHTML')
        print('name:', name)
        return name

    def _get_original_price(self):
        ORIGIN_PRICE_CLASS = '_3_ISdg'
        self._wait(ORIGIN_PRICE_CLASS)

        xpath = "//div[@class='{}']".format(ORIGIN_PRICE_CLASS)
        price_tag = self.driver.find_element_by_xpath(xpath)
        price = price_tag.get_attribute('innerHTML')
        print('price:', price)
        return price

    def _get_sale_price(self):
        try:
            SALE_PRICE_CLASS = '_3n5NQx'
            self._wait(SALE_PRICE_CLASS)
            xpath = "//div[@class='{}']".format(SALE_PRICE_CLASS)
            price_tag = self.driver.find_element_by_xpath(xpath)
            price = price_tag.get_attribute('innerHTML')
            print('sale price:', price)
            return price
        except Exception:
            return None


if __name__ == '__main__':
    driver = ShoppeMerchandisePageScrapy.get_driver()
    url = 'https://shopee.tw/%E3%80%90%E5%85%A8%E6%96%B0%E3%80%91-PS4-Slim-500GB-1TB-%E7%99%BD-%E9%BB%91-%E4%B8%BB%E6%A9%9F-%E5%8F%B0%E7%81%A3%E5%85%AC%E5%8F%B8%E8%B2%A8-CUH-2218A-%E5%8F%AF%E9%9D%A2%E4%BA%A4-Pro-%E9%AD%94%E7%89%A9%E7%8D%B5%E4%BA%BA-i.14159223.1326072367'
    smpc = ShoppeMerchandisePageScrapy(driver)
    smpc.parse(url)
