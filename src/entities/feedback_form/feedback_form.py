import abc


class FeedBackForm(metaclass=abc.ABCMeta):
    def __init__(self):
        self.amount = None
        self.pct = None
        self.md = None

    @abc.abstractmethod
    def feedback(self, price=None):
        pass

    def to_dict(self):
        return {
            'amount': self.amount,
            'pct': self.pct,
            'md': self.md
        }