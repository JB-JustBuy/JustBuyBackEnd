from src.entities.scrapy.searching_merchandise_page_scrapy import MerchandisePageScrapy
import time


class ShoppeMerchandisePageScrapy(MerchandisePageScrapy):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.PLAT_FORM = 'shoppe'


    def parse(self, url):
        self.driver.get(url)
        time.sleep(1)

        name = self._get_name()
        price = self._get_origin_price()
        sale_price = self._get_sale_price()
        md = {
            'name': name,
            'price': price,
            'sale_price': sale_price,
            'platform': self.PLAT_FORM,
            'url': url
        }
        return md

    def _get_name(self):
        NAME_ClASS = 'qaNIZv'
        xpath = "//div[@class='{}']".format(NAME_ClASS)
        name_div = self.driver.find_element_by_xpath(xpath)
        name = name_div.find_element_by_xpath('span').get_attribute('innerHTML')
        print('name:', name)
        return name

    def _get_origin_price(self):
        ORIGIN_PRICE_CLASS = '_3_ISdg'
        xpath = "//div[@class='{}']".format(ORIGIN_PRICE_CLASS)
        price_tag = self.driver.find_element_by_xpath(xpath)
        price = price_tag.get_attribute('innerHTML')
        print('price:', price)
        return price

    def _get_sale_price(self):
        try:
            ORIGIN_PRICE_CLASS = '_3n5NQx'
            xpath = "//div[@class='{}']".format(ORIGIN_PRICE_CLASS)
            price_tag = self.driver.find_element_by_xpath(xpath)
            price = price_tag.get_attribute('innerHTML')
            print('sale price:', price)
            return price
        except Exception:
            return None


if __name__ == '__main__':
    url = 'https://shopee.tw/%E3%80%90%E5%85%A8%E6%96%B0%E3%80%91-PS4-Slim-500GB-1TB-%E7%99%BD-%E9%BB%91-%E4%B8%BB%E6%A9%9F-%E5%8F%B0%E7%81%A3%E5%85%AC%E5%8F%B8%E8%B2%A8-CUH-2218A-%E5%8F%AF%E9%9D%A2%E4%BA%A4-Pro-%E9%AD%94%E7%89%A9%E7%8D%B5%E4%BA%BA-i.14159223.1326072367'
    smpc = ShoppeMerchandisePageScrapy()
    smpc.parse(url)