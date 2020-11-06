from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time, os


class PChomeDataController(object):
    def __init__(self, driver_path=None):
        self.url = "https://ecshweb.pchome.com.tw/search/v3.3/?q="
        self.save_path = os.path.abspath(os.path.join("..", "..", "data"))
        if driver_path is None:
            self.driver_path = os.path.abspath(os.path.join(os.path.pardir, 'chromedriver'))
        else:
            self.driver_path = driver_path
        self.driver = self.get_driver()
        self.platform = "pchome"
        self.products = []

    def login(self):
        pass

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def get_driver(self):
        options = self.get_chrome_options()
        driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        return driver

    def get_chrome_options(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': self.save_path,
                 'directory_upgrade': True}
        options.add_experimental_option('prefs', prefs)

        # hide the web driver window
        #options.add_argument("--headless")
        return options

    def search(self, search_key):
        self.driver.get(self.url+search_key)
        time.sleep(3)
        self.parser()
        self.driver.quit()

    def parser(self):
        elem_item_contain = self.driver.find_element_by_xpath('//div[@id="ItemContainer"]')
        elem_items = elem_item_contain.find_elements_by_tag_name('dl')
        for index, elem_item in enumerate(elem_items):
            name = self.get_name(elem_item)
            price = self.get_price(elem_item)
            url = self.get_url(elem_item)
            print("Index:", index)
            print(" name:{}, platform:{} ,price:{},\n url:{}\n".format(name, self.platform,price, url))
            self.products.append({"name": name, "price": price, "url": url, "platform": self.platform})

    def get_name(self, elem):
        elem_name = elem.find_element_by_class_name('prod_name')
        elem_a = elem_name.find_element_by_tag_name('a')
        name = elem_a.get_attribute('innerHTML').splitlines()[0].replace("</em>", "").replace("<em>", "")
        return name

    def get_url(self, elem):
        elem_name = elem.find_element_by_class_name('prod_name')
        elem_a = elem_name.find_element_by_tag_name('a')
        return elem_a.get_attribute('href')

    def get_price(self, elem):
        elem_price = elem.find_element_by_class_name('price')
        elem_value = elem_price.find_element_by_class_name("value")
        price = elem_value.get_attribute("innerHTML").splitlines()[0]
        return price

if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.path.pardir, '../chromedriver')))
    dc = PChomeDataController()
    dc.search('羅技G604')
