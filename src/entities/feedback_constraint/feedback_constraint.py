import abc


class FeedBackConstraint(metaclass=abc.ABCMeta):
    def __init__(self):
        self.amount = None
        self.platform = None
        self.md_type = None
        self.quantity = None
    @abc.abstractmethod
    def qualify(self, merchandises):
        pass

