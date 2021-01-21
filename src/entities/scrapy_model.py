from src.entities.scrapy.scrapy import Scrapy
from src.generator.searching_engine_scrapy import SearchingEngineScrapyGenerator
from src.generator.merchandise_page_scrapy_generator import MerchandisePageScrapyGenerator
from src.utilies.parser.url_parser import UrlParser


class ScrapyModel:
    def __init__(self):
        self.driver = Scrapy.get_driver()
        self.__scrapies = {}
        self.__acception = ["shopee", 'pchome']
        self.keywords = None
        self.md_by_url = {}



    @property
    def scrapies(self):
        return self.__scrapies

    def search(self, urls):
        # 搜尋使用者相要商品的url
        self.get_merchandises_by_urls(urls)
        print(self.md_by_url)
        keywords = [md['name'] for url, md in self.md_by_url.items()]

        # 在所有平台搜尋相似產品
        self.search_products_in_platform_engine(keywords, 'all')

        # quit is close all tab in driver
        self.driver.quit()
        
    def get_merchandises_by_urls(self, urls):
        print('urls:', urls)
        for url in urls:
            merchandise = self.get_merchandise_by_url(url)
            print('get', merchandise, 'from', url)
            self.md_by_url.update({url: merchandise})

    def get_merchandise_by_url(self, url: str):
        url_platform = UrlParser.recognize_platform(url)
        if url_platform in self.__scrapies.keys():
            return self.__scrapies[url_platform]['md_page_scrapy'].parse(url)
        else:
            raise ValueError("Cant find {} scraper in Scrapy Model".format(url_platform))

    def search_products_in_platform_engine(self, keywords: list, scrapy_key: str):
        self.keywords = keywords
        print('keywords:', self.keywords)
        if scrapy_key == 'all':
            for key, scrapy_dict in self.__scrapies.items():
                print('By {} engine searching result:'.format(key))
                scrapy_dict['engine_scrapy'].search(keywords)

        else:
            scrapy_dict = self.__scrapies[scrapy_key]
            scrapy_dict['engine_scrapy'].search(keywords)

    def add_scrapy(self, name: str):
        if name in self.__acception:
            self.__scrapies[name] = {}
            self.__scrapies[name]['engine_scrapy'] = SearchingEngineScrapyGenerator.generate_scrapy(name, self.driver)
            self.__scrapies[name]['md_page_scrapy'] = MerchandisePageScrapyGenerator.generate_scrapy(name, self.driver)
        else:
            raise ValueError("scrapy model add_scrapy:: {} is not validate".format(name))

    @staticmethod
    def generate_scrapy_model(platforms: str or list):
        model = ScrapyModel()
        if isinstance(platforms, str):
            if platforms == 'all':
                model.add_scrapy('pchome')
                model.add_scrapy('shopee')
                return model
            else:
                 raise ValueError("model' paras:: content can't use str except 'all'")
        elif isinstance(platforms, list):
            for name in platforms:
                model.add_scrapy(name)
                return model
        else:
            raise ValueError("model' paras:: content value error")

    def __dict__(self):
        return {
            'acceptable': self.__acception,
            'scrapies': self.__scrapies,
            'keywords': self.keywords,
            'md_by_url': self.md_by_url
        }





if __name__ == '__main__':
    import json
    model = ScrapyModel.generate_scrapy_model('all')
    #
    urls = ["https://24h.pchome.com.tw/prod/DGBJA7-A9009QSCJ",
            "https://24h.pchome.com.tw/prod/DYAQ12-A9008MMZF"]
    model.search(urls)
    print(model.__dict__())

