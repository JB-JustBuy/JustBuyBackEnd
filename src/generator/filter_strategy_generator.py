from src.entities.merchandise import filter_merchdise_strategy
from src.entities.merchandise.merchandise import Merchandise


class FilterStrategyGenerator:
    @staticmethod
    def generate_strategy(strategy_type: str, reference_merchandise: Merchandise, **kwargs):
        if strategy_type == 'cheap':
            return filter_merchdise_strategy.CheapFilterStrategy(reference_merchandise)
        elif strategy_type == 'familiar':
            if "price_range" in kwargs:
                price_range = kwargs['price_range'] if isinstance(kwargs['price_range'], float) and \
                            0 <= kwargs['price_range'] <= 1 else 0.1
                return filter_merchdise_strategy.FamiliarFilterStrategy(reference_merchandise, price_range)
            else:
                return filter_merchdise_strategy.FamiliarFilterStrategy(reference_merchandise, 0.3)
        elif strategy_type == 'up_limit':
            if "up_limit" in kwargs and isinstance(kwargs['up_limit'], int):
                up_limit = kwargs['up_limit']
                return filter_merchdise_strategy.UpLimitFilterStrategy(up_limit)
            return filter_merchdise_strategy.UpLimitFilterStrategy(5)
        else:
            raise ValueError("strategy_type is not acceptable")