from src.entities.scrapy.scrapy import Scrapy
import abc


class MerchandisePageScrapy(Scrapy):
    def __int__(self, driver):
        super().__init__(driver)

    @abc.abstractmethod
    def parse(self, url):
        pass