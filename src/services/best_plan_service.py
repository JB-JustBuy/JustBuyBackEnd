from src.entities.disocunt_model import DiscountModel
from src.entities.scrapy_model import ScrapyModel, Scrapy
from src.entities.merchandise import filter_merchdise_strategy

class BestPlanService:
    def __init__(self, urls: list, selected_strategy: str):
        self.urls = urls
        self.selected_strategy = selected_strategy

    def plan(self):
        print("Start plan service")
        # define scrapy model
        scrapy_model = ScrapyModel.generate_scrapy_model('all')
        print("Generate Scrapy Model")

        scrapy_model.search(self.urls)
        # create planning model
        # model = DiscountModel(scrapy_model)

        # new model and calculate best plan
        # result = model.analysis()
        print("End plan service")
        return 0

    def test(self):
        driver = Scrapy.get_driver()
        return 200
