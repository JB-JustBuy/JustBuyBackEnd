import abc


class FeedBackConstraint(metaclass=abc.ABCMeta):
    def __init__(self):
        self.constraint = None
        self.platform = None

    @abc.abstractmethod
    def is_satisfied(self, merchandises):
        pass
