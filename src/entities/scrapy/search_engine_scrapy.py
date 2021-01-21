from src.entities.scrapy.scrapy import Scrapy
import abc, time, logging


class SearchEngineScrapy(Scrapy):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = None
        self.platform = None
        self.result = {}

    def search(self, search_keys):
        logging.info(__name__+' start search:')
        for search_key in search_keys:
            # open new window
            self.switch_to_new_tab(self.url+search_key, self.driver)
            time.sleep(2)

            # scrapy the info on web
            products = self.parse()

            # close tab in driver
            self.result[search_key] = products

        logging.info(__name__+' end search')

    @abc.abstractmethod
    def parse(self):
        pass