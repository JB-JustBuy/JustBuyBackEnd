from src.entities.scrapy.shoppe_merchandise_page_scrapy import ShoppeMerchandisePageScrapy
from src.entities.scrapy.pchome_merchandise_page_scrapy import PchomeMerchandisePageScrapy


class MerchandisePageScrapyGenerator:
    @staticmethod
    def generate_scrapy(platform: str):
        if platform == 'shopee':
            return ShoppeMerchandisePageScrapy()
        elif platform == 'pchome':
            return PchomeMerchandisePageScrapy()
        else:
            raise ValueError('Cant generate {} merchandise page scrapy'.format(platform))
