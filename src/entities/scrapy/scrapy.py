from selenium import webdriver
import abc, time, logging
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager



class Scrapy(metaclass=abc.ABCMeta):
    def __init__(self,):
        self.url = None
        self.save_path = None
        self.driver = None
        self.platform = None
        self.result = {}

    def search(self, search_keys):
        logging.info(__name__+' start search:')
        for search_key in search_keys:
            self.driver.get(self.url+search_key)
            time.sleep(3)
            self.parser()
            products = self.parser()
            self.result[search_key] = products
        self.driver.quit()
        logging.info(__name__+' end search')


    def get_driver(self):
        options = self.get_chrome_options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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