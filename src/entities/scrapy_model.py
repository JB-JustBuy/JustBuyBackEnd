from src.entities.scrapy.search_engine_scrapy import SearchEngineScrapy
from src.entities.scrapy.pchome_searching_engine_scrapy import PChomeSearchingEngineScrapy
from src.entities.scrapy.shoppe_searching_engine_scrapy import ShoppeSearchingEngineScrapy


class ScrapyModel:
    def __init__(self):
        self.__scrapies = {}
        self.__acception = ["shoppe", 'pchome']

    @property
    def scrapies(self):
        return self.__scrapies

    def search(self, keywords: list, scrapy_key: str):
        if scrapy_key == 'all':
            for key, scrapy_dict in self.__scrapies.items():
                scrapy_dict['scrapy'].search(keywords)
        else:
            scrapy_dict = self.__scrapies[scrapy_key]
            scrapy_dict['scrapy'].search(keywords)

    def add_scrapy(self, name: str):
        if name in self.__acception:
            self.__scrapies[name] = {}
            if name == 'shoppe':
                self.__scrapies[name]['scrapy'] = ShoppeSearchingEngineScrapy()

            elif name == 'pchome':
                self.__scrapies[name]['scrapy'] = PChomeSearchingEngineScrapy()
        else:
            raise ValueError("scrapy model add_scrapy:: name is not validate'")

    @staticmethod
    def generate_scrapy_model(platforms: str or list):
        model = ScrapyModel()
        if isinstance(platforms, str):
            if platforms == 'all':
                model.add_scrapy('pchome')
                model.add_scrapy('shoppe')
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
            'scrapies': self.__scrapies
        }
if __name__ == '__main__':
    import json
    model = ScrapyModel.generate_scrapy_model('all')
    model.search(scrapy_key='all', keywords=['羅技G604'])
    dict = model.__dict__()
    print(dict)