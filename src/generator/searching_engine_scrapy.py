from src.entities.scrapy.pchome_searching_engine_scrapy import PChomeSearchingEngineScrapy
from src.entities.scrapy.shoppe_searching_engine_scrapy import ShoppeSearchingEngineScrapy


class SearchingEngineScrapyGenerator:
    @staticmethod
    def generate_scrapy(platform, driver=None):
        if platform == 'shopee':
            return ShoppeSearchingEngineScrapy(driver)
        elif platform == 'pchome':
            return PChomeSearchingEngineScrapy(driver)
        else:
            raise ValueError('Cant generate {} searching engine scrapy'.format(platform))
