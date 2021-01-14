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
        output = {}
        if self.amount is not None:
            output['amount'] = self.amount
        if self.pct is not None:
            output['pct'] = self.pct
        if self.md is not None:
            output['md'] = self.md.to_dict()

        return {
            'amount': self.amount,
            'pct': self.pct,
            'md': self.md
        }