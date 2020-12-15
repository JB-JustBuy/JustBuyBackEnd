from src.entities.scrapy.scrapy import Scrapy
import abc, time, logging


class SearchEngineScrapy(Scrapy):
    def __init__(self,):
        super().__init__()
        self.url = None
        self.platform = None
        self.result = {}

    def search(self, search_keys):
        logging.info(__name__+' start search:')
        for search_key in search_keys:
            self.driver.get(self.url+search_key)
            time.sleep(3)
            self.parse()
            products = self.parse()
            self.result[search_key] = products
        self.driver.quit()
        logging.info(__name__+' end search')

    @abc.abstractmethod
    def parse(self):
        pass