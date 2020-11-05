import abc


class Payment(metaclass=abc.ABCMeta):
    def __init__(self):
        self.methods = None

