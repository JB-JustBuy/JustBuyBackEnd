from src.entities.scrapy.searching_merchandise_page_scrapy import SearchingMerchandisePageScrapy
import time


class ShoppeMerchandisePageScrapy(SearchingMerchandisePageScrapy):
    def __init__(self):
        super().__init__()
        self.driver = self.get_driver()
        self.PLAT_FORM = 'shoppe'

    def parse(self, url):
        self.driver.get(url)
        time.sleep(1)

        name = self._get_name()
        price = self._get_origin_price()
        sale_price = self._get_sale_price()
        self.driver.quit()
        return {
            'name': name,
            'price': price,
            'sale_price': sale_price,
            'platform': self.PLAT_FORM,
            'url': url
        }

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
            return price
        except Exception as e:
            return None


if __name__ == '__main__':
    url = 'https://shopee.tw/EDWIN-503%E5%9F%BA%E6%9C%AC%E4%BA%94%' \
          'E8%A2%8B%E7%AA%84%E7%9B%B4%E7%AD%92%E7%89%9B%E4%BB%94%E8%A4%B2(%E5%8E%9F%E8%97%8D%E8%89%B2)' \
          '-%E7%94%B7%E6%AC%BE-i.135828246.2283224945'
    smpc = ShoppeMerchandisePageScrapy()
    smpc.search(url)