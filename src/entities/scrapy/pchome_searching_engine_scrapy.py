from src.entities.scrapy.search_engine_scrapy import SearchEngineScrapy
import os


class PChomeSearchingEngineScrapy(SearchEngineScrapy):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ecshweb.pchome.com.tw/search/v3.3/?q="
        self.driver = self.get_driver()
        self.platform = "pchome"

    def parse(self):
        elem_item_contain = self.driver.find_element_by_xpath('//div[@id="ItemContainer"]')
        elem_items = elem_item_contain.find_elements_by_tag_name('dl')
        products = []
        for index, elem_item in enumerate(elem_items):
            name = self._get_name(elem_item)
            price = self._get_price(elem_item)
            url = self._get_url(elem_item)
            print("Index:", index)
            print(" name:{}, platform:{} ,price:{},\n url:{}\n".format(name, self.platform, price, url))
            products.append({"name": name, "price": price, "url": url, "platform": self.platform})

        return products

    def _get_name(self, elem):
        elem_name = elem.find_element_by_class_name('prod_name')
        elem_a = elem_name.find_element_by_tag_name('a')
        name = elem_a.get_attribute('innerHTML').splitlines()[0].replace("</em>", "").replace("<em>", "")
        return name

    def _get_url(self, elem):
        elem_name = elem.find_element_by_class_name('prod_name')
        elem_a = elem_name.find_element_by_tag_name('a')
        return elem_a.get_attribute('href')

    def _get_price(self, elem):
        elem_price = elem.find_element_by_class_name('price')
        elem_value = elem_price.find_element_by_class_name("value")
        price = int(elem_value.get_attribute("innerHTML").splitlines()[0].replace(',', ""))
        return price

if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    dc = PChomeSearchingEngineScrapy()
    dc.search(['羅技G604'])
    print(dc.result)
