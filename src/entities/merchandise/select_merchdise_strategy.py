from src.entities.merchandise.merchandise import Merchandise
import numpy as np
import abc


class StrategyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_ideal(self, merchandises: list):
        pass


class CheapestStrategy(StrategyInterface):
    def find_ideal(self, merchandises: list):
        prices = []
        for merchandise in merchandises:
            print('merchandise:', merchandise)
            if isinstance(merchandise, Merchandise):
                prices.append(merchandise.price)
            else:
                raise TypeError("Type of merchandises element need to be Merchandise")
        return merchandises[np.argmin(prices)]


class FamiliarPriceStrategy(StrategyInterface):
    def __init__(self, price, percentage, selected='max'):
        self.percentage = percentage
        self.price = price
        self.selected = selected

    def find_ideal(self, merchandises: list):
        quantified = []
        for merchandise in merchandises:
            if isinstance(merchandise, Merchandise):
                if (self.price * 1 - self.percentage) <= merchandise.price <= (self.price * 1 + self.percentage):
                    quantified.append(merchandise)
            else:
                raise TypeError("Type of merchandises element need to be Merchandise")
        prices = [md.price for md in quantified]
        if self.selected == 'min':
            return quantified[np.argmin(prices)]
        elif self.selected == 'max':
            return quantified[np.argmax(prices)]

