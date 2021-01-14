from src.entities.feedback_constraint.feedback_constraint import FeedBackConstraint
from src.entities.merchandise.merchandise import Merchandise


class QuantityEnough(FeedBackConstraint):
    def __init__(self, quantity: int, platform: str, md_type: str):
        super().__init__()
        self.name = "買{}件商品".format(quantity)
        self.quantity = quantity
        self.platform = platform
        self.md_type = md_type

    def qualify(self, merchandises: list):
        """
            確認是否滿足”五件相同商品“
        :param merchandises: list, contain <Merchandise> element
        :return: bool
        """
        for md in merchandises:
            if self._is_quantity_conform(md) and self._is_platform_conform(md) and  self._is_md_type_conform(md):
                return True
        return False


    def _is_quantity_conform(self, merchandise: Merchandise):
        return merchandise.quantity >= self.quantity

    def _is_platform_conform(self, merchandise: Merchandise):
        return merchandise.platform == self.platform if self.platform else True

    def _is_md_type_conform(self, merchandise: Merchandise):
        return merchandise.md_type == self.md_type if self.md_type else True