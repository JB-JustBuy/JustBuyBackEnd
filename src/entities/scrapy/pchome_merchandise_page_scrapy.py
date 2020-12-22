from src.entities.scrapy.searching_merchandise_page_scrapy import MerchandisePageScrapy


class PchomeMerchandisePageScrapy(MerchandisePageScrapy):
    def __int__(self, driver):
        super().__init__(driver)
        self.PLAFORM = 'pchome'

    def parse(self, url):
        self.driver.get(url)
        self._wait('prod_describe')
        name = self.__get_name()
        price = self.__get_original_price()
        sale_price = self.__get_sale_price()
        print('from url:{}'.format(url))
        print(' name: {}\n price: {}\n sale_price: {}'.format(name, price, sale_price))
        return {
            'name': name,
            'price': price,
            'sale_price': sale_price
        }

    def __get_name(self):
        prod = self.driver.find_element_by_xpath('//div[@class="prod_describe"]')
        try:
            # name = prod.find_element_by_xpath('//h5[@class="nick"]').get_attribute('innerHTML').split('<br>')[1]
            name = prod.find_element_by_xpath('//h5[@class="nick"]').text
            return name
        except:
            return name

    def __get_original_price(self):
        price_box = self.driver.find_element_by_xpath('//ul[@class="price_box"]')
        text = price_box.find_element_by_xpath('//li[@class="original"]').text
        origin_price = text.split('$')[1]
        return origin_price

    def __get_sale_price(self):
        price_box = self.driver.find_element_by_xpath('//ul[@class="price_box"]')
        sale_price = price_box.find_element_by_xpath('//span[@id="PriceTotal"]').text
        return sale_price


if __name__ == '__main__':
    driver = PchomeMerchandisePageScrapy.get_driver()
    url = 'https://24h.pchome.com.tw/prod/DGBJA7-1900B1QBE'
    scrapy = PchomeMerchandisePageScrapy(driver)
    scrapy.parse(url)
    driver.quit()