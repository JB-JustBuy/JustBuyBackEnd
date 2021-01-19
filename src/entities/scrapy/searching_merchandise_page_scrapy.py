from src.entities.scrapy.scrapy import Scrapy
import abc


class MerchandisePageScrapy(Scrapy):
    def __int__(self):
        super().__init__()

    @abc.abstractmethod
    def parse(self, url):
        pass