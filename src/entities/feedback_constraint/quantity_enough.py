from src.entities.feedback_constraint.feedback_constraint import FeedBackConstraint

class QuantityEnough(FeedBackConstraint):
    def __init__(self, quantity, platform, md_type):
        self.quantity = quantity
        self.platform = platform
        self.md_type = md_type

    def qualify(self, merchandises):
        """
            確認是否滿足”五件相同商品“
        :param merchandises: list, contain <Merchandise> element
        :return: bool
        """
        for md in merchandises:
            if self._is_quantity_conform(md) and self._is_platform_conform(md) and  self._is_md_type_conform(md):
                return True
        return False


    def _is_quantity_conform(self, merchandise):
        return merchandise.quantity >= self.quantity

    def _is_platform_conform(self, merchandise):
        return merchandise.platform == self.platform if self.platform else True

    def _is_md_type_conform(self, merchandise):
        return merchandise.md_type == self.md_type if self.md_type else True