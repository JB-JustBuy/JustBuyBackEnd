from src.entities.merchandise.merchandise import Merchandise
import abc


class FilterStrategyInterface(metaclass=abc.ABCMeta):
    def __init__(self, reference_merchandise, price_range=None, platform=None):
        self.ref_md = reference_merchandise
        self.price_range = price_range
        self.platform = platform

    @abc.abstractmethod
    def filter(self, merchandises: list):
        pass


class CheapFilterStrategy(FilterStrategyInterface):
    def __init__(self, reference_merchandise, price_range=None, platform=None):
        super().__init__(reference_merchandise, price_range, platform)

    def filter(self, merchandises: list):
        confirmed_md = []
        for merchandise in merchandises:
            if self.__is_cheap(merchandise) and \
                    self.__is_same_platform(merchandise):
                confirmed_md.append(merchandise)
        return confirmed_md

    def __is_cheap(self, merchandise: Merchandise):
        return merchandise.price <= self.ref_md.price

    def __is_same_platform(self, merchandise: Merchandise):
        if self.platform is None:
            return True
        else:
            return merchandise.platform == self.platform


class FamiliarFilterStrategy(FilterStrategyInterface):
    def __init__(self, reference_merchandise, price_range=0.1, platform=None):
        super().__init__(reference_merchandise, price_range, platform)

    def filter(self, merchandises: list):
        confirmed_md = []
        for merchandise in merchandises:
            print('find md price:{} and ref_md price:{}'.format(merchandise.price,
                                                                self.ref_md.price))
            if self.__is_in_price_range(merchandise) and \
                self.__is_same_platform(merchandise):

                confirmed_md.append(merchandise)
        return confirmed_md

    def __is_in_price_range(self, merchandise: Merchandise):
        return self.ref_md.price * 1 - self.price_range <= merchandise.price \
               <= self.ref_md.price * 1 + self.price_range

    def __is_same_platform(self, merchandise: Merchandise):
        if self.platform is None:
            return True
        else:
            return merchandise.platform == self.platform

