from selenium import webdriver
import abc, time
from selenium.webdriver import ActionChains



class Scraper(metaclass=abc.ABCMeta):
    def __init__(self,):
        self.url = None
        self.save_path = None
        self.driver_path = None
        self.driver = None
        self.platform = None
        self.result = {}

    def search(self, search_keys):
        for search_key in search_keys:
            self.driver.get(self.url+search_key)
            time.sleep(3)
            self.parser()
            products = self.parser()
            self.result[search_key] = products
        self.driver.quit()

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

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()


    @abc.abstractmethod
    def parser(self):
        pass