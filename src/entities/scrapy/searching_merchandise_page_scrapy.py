from src.entities.scrapy.scrapy import Scrapy
import abc


class SearchingMerchandisePageScrapy(Scrapy):
    def __int__(self):
        super().__init__()

    @abc.abstractmethod
    def parse(self, url):
        pass