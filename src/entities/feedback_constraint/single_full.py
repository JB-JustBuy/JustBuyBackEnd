from src.entities.feedback_constraint.feedback_constraint import FeedBackConstraint


class SingleFull(FeedBackConstraint):
    def __init__(self, amount, platform=None, md_type=None):
        super().__init__()
        self.amount = amount
        self.platform = platform
        self.md_type = md_type

    def qualify(self, merchandises):
        """
            確認是否滿足“單筆滿額”的限制
        :param merchandises: list,
        :return: bool
        """
        for merchandise in merchandises:
            print("amount:{}, platform:{}, qualified:{}".format(self.amount, self.platform, self._is_amount_conform(merchandise) and\
                    self._is_platform_conform(merchandise) and\
                    self._is_md_type_conform(merchandise)))
            if self._is_amount_conform(merchandise) and\
                    self._is_platform_conform(merchandise) and\
                    self._is_md_type_conform(merchandise):

                return True
        return False

    def _is_amount_conform(self, merchandise):

        return merchandise.price >= self.amount if self.amount else True

    def _is_platform_conform(self, merchandise):
        return merchandise.platform == self.platform if self.platform else True

    def _is_md_type_conform(self, merchandise):
        return merchandise.type == self.platform if self.md_type else True
