import abc


class FeedBackConstraint(metaclass=abc.ABCMeta):
    def __init__(self):
        self.amount = None
        self.platform = None
        self.md_type = None
        self.quantity = None

    @abc.abstractmethod
    def qualify(self, merchandises: list):
        pass

    def to_dict(self):
        return {
            "quantity": self.quantity,
            'platform': self.platform,
            'md_type': self.md_type,
            'amount': self.amount
        }