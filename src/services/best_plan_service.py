from src.entities.disocunt_model import DiscountModel
from src.entities.scrapy_model import ScrapyModel
from src.entities.merchandise import filter_merchdise_strategy


class BestPlanService:
    def __int__(self, urls: list, selected_strategy: str):
        self.urls = urls
        self.selected_strategy = selected_strategy

    def plan(self):
        # define scrapy model
        scrapy_model = ScrapyModel.generate_scrapy_model('all')

        # create planning model
        model = DiscountModel(scrapy_model, 'familiar')

        # new model and calculate best plan
        model.calculate()
