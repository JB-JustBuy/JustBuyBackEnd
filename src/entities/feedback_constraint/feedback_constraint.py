import abc


class FeedBackConstraint(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = None
        self.amount = None
        self.platform = None
        self.md_type = None
        self.quantity = None

    @abc.abstractmethod
    def qualify(self, merchandises: list):
        pass

    def to_dict(self):
        output = {}
        if self.name is not None:
            output['name'] = self.name
        if self.amount is not None:
            output['amount'] = self.amount
        if self.platform is not None:
            output['platform'] = self.platform
        if self.md_type is not None:
            output['md_type'] = self.md_type
        if self.quantity is not None:
            output['quantity'] = self.quantity
        return output