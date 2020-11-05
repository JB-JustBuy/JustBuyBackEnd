from src.feedback_constraint.feedback_constraint import FeedBackConstraint


class SingleFull(FeedBackConstraint):
    def __init__(self, amount, platform=None):
        super().__init__()
        self.amount = amount
        self.platform = platform

    def is_satisfied(self, merchandises):
        for merchandise in merchandises:
            if self._is_amount_conform(merchandise) and self._is_platform_conform(merchandise):
                return True
        return False

    def _is_amount_conform(self, merchandise):
        return merchandise.price >= self.amount if self.amount else True

    def _is_platform_conform(self, merchandise):
        return merchandise.platform == self.platform if self.platform else True
