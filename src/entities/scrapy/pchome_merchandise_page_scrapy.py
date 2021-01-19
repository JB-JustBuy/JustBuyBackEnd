from src.entities.scrapy.searching_merchandise_page_scrapy import MerchandisePageScrapy


class PchomeMerchandisePageScrapy(MerchandisePageScrapy):
    def __init__(self):
        super().__init__()
        self.platform = 'pchome'

    def parse(self, url):
        self.driver.get(url)
        self._wait('prod_describe')
        name = self.__get_name()
        original_price = self.__get_original_price()
        sale_price = self.__get_sale_price()
        print('from url:{}'.format(url))
        print(' name: {}\n original_price: {}\n sale_price: {}'.format(name, original_price, sale_price))

        if sale_price is not None:
            price = sale_price
        elif original_price is not None:
            price = original_price
        else:
            price = None
        return {
            'name': name,
            'price': price,
            'platform': self.platform,
            'url': url
        }

    def __get_name(self):
        prod = self.driver.find_element_by_xpath('//div[@class="prod_describe"]')
        try:
            # name = prod.find_element_by_xpath('//h5[@class="nick"]').get_attribute('innerHTML').split('<br>')[1]
            name = prod.find_element_by_xpath('//h5[@class="nick"]').text.splitlines()[1]

            return name
        except:
            return None

    def __get_original_price(self):
        try:
            price_box = self.driver.find_element_by_xpath('//ul[@class="price_box"]')
            text = price_box.find_element_by_xpath('//li[@class="original"]').text
            origin_price = text.split('$')[1]
            return origin_price
        except Exception:
            return None

    def __get_sale_price(self):
        try:
            price_box = self.driver.find_element_by_xpath('//ul[@class="price_box"]')
            sale_price = price_box.find_element_by_xpath('//span[@id="PriceTotal"]').text
            return sale_price
        except Exception:
            return None



if __name__ == '__main__':
    driver = PchomeMerchandisePageScrapy.get_driver()
    url = 'https://24h.pchome.com.tw/prod/DGBJA7-1900B1QBE'
    scrapy = PchomeMerchandisePageScrapy(driver)
    scrapy.parse(url)
    driver.quit()