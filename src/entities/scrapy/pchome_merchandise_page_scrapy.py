from src.entities.scrapy.searching_merchandise_page_scrapy import MerchandisePageScrapy


class PchomeMerchandisePageScrapy(MerchandisePageScrapy):
    def __int__(self, driver):
        super().__init__(driver)

    def parse(self, url):
        pass