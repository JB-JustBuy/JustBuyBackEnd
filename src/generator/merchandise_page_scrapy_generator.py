from src.entities.scrapy.shoppe_merchandise_page_scrapy import ShoppeMerchandisePageScrapy
from src.entities.scrapy.pchome_merchandise_page_scrapy import PchomeMerchandisePageScrapy


class MerchandisePageScrapyGenerator:
    @staticmethod
    def generate_scrapy(platform: str, driver=None):
        if platform == 'shopee':
            return ShoppeMerchandisePageScrapy(driver)
        elif platform == 'pchome':
            return PchomeMerchandisePageScrapy(driver)
        else:
            raise ValueError('Cant generate {} merchandise page scrapy'.format(platform))
