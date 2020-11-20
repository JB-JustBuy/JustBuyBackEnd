import abc


class FeedBackForm(metaclass=abc.ABCMeta):
    def __init__(self):
        self.amount = None
        self.pct = None
        self.md = None

    @abc.abstractmethod
    def feedback(self, price=None):
        pass
