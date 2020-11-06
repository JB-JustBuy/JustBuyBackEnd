from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time, os


class ShoppeDataController(object):
    def __init__(self, driver_path=None):
        self.url = "https://shopee.tw/search?keyword="
        self.save_path = os.path.abspath(os.path.join("..", "..", "data"))
        if driver_path is None:
            self.driver_path = os.path.abspath(os.path.join(os.path.pardir, 'chromedriver'))
        else:
            self.driver_path = driver_path
        self.driver = self.get_driver()
        self.platform = "shoppe"
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
        options.add_argument("--headless")
        return options

    def search(self, search_key):
        self.driver.get(self.url+search_key)
        time.sleep(3)
        self.parser()
        self.driver.quit()

    def parser(self):
        elem_row = self.driver.find_element_by_xpath("//div[@class='row shopee-search-item-result__items']")
        elem_names = elem_row.find_elements_by_xpath('//div[@class="_1NoI8_ _16BAGk"]')
        elem_ads = elem_row.find_elements_by_xpath('//div[@data-sqe="ad"]')
        elem_links = elem_row.find_elements_by_xpath('//a[@data-sqe="link"]')
        elem_prices = elem_row.find_elements_by_xpath('//*[@class="_341bF0"]')

        for index, (name, link, price) in enumerate(zip(elem_names, elem_links, elem_prices)):
            print("Index:", index)
            print(' name:{}, platform:{}, price:{}\n link:{}\n'.format(name.get_attribute("innerHTML").splitlines()[0],
                                                                    self.platform,
                                                                    price.get_attribute("innerHTML").splitlines()[0],
                                                                    link.get_attribute("href")))
            if index >= len(elem_ads):
                product = {
                    "name": name.get_attribute("innerHTML").splitlines()[0],
                    "price":  price.get_attribute("innerHTML").splitlines()[0],
                    "url": link.get_attribute("href"),
                    "platform": self.platform
                }
                self.products.append(product)

    def get_name(self, elem):
        pass

    def get_price(self, elem):
        pass

if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.path.pardir, '../chromedriver')))
    dc = ShoppeDataController()
    dc.search('羅技G604')
    print(dc.products)
