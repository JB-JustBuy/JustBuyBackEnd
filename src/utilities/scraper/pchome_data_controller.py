from src.utilities.scraper.scraper import Scraper
import os


class PChomeDataController(Scraper):
    def __init__(self, driver_path=None):
        super().__init__()
        self.url = "https://ecshweb.pchome.com.tw/search/v3.3/?q="
        self.save_path = os.path.abspath(os.path.join("../../..", "..", "data"))
        if driver_path is None:
            self.driver_path = os.path.abspath(os.path.join(os.path.pardir, 'chromedriver'))
        else:
            self.driver_path = driver_path
        self.driver = self.get_driver()
        self.platform = "pchome"
        self.result = {}

    def parser(self):
        elem_item_contain = self.driver.find_element_by_xpath('//div[@id="ItemContainer"]')
        elem_items = elem_item_contain.find_elements_by_tag_name('dl')
        products = []
        for index, elem_item in enumerate(elem_items):
            name = self._get_name(elem_item)
            price = self._get_price(elem_item)
            url = self._get_url(elem_item)
            print("Index:", index)
            print(" name:{}, platform:{} ,price:{},\n url:{}\n".format(name, self.platform,price, url))
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
        price = elem_value.get_attribute("innerHTML").splitlines()[0]
        return price

if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.path.pardir, '../../../chromedriver')))
    dc = PChomeDataController()
    dc.search(['羅技G604'])
    print(dc.result)
