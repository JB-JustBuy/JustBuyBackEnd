from src.feedback_method.feedback_method import FeedBackMethod
import abc
import numpy as np


class Payment(metaclass=abc.ABCMeta):
    def __init__(self):
        self.methods = []
        self.name = None
        self.type = None

    def add_method(self, method):
        if isinstance(method, FeedBackMethod):
            self.methods.append(method)
        else:
            raise TypeError("Paras: 'method' is not FeedBackMethod!")

    def get_best_method(self, methods):
        feedback = [method.feedback() for method in methods]
        print(" feedback:", feedback)
        idx = np.argmax(feedback)
        print(" index:", idx)
        return methods[idx]

    def get_qualified_best_method(self, merchandises, methods):
        print("Methods:", methods)
        qualified_methods = []
        for method in methods:
            if method.qualify(merchandises):
                qualified_methods.append(method)
        print("Qualified Methods:", methods)
        return self.get_best_method(qualified_methods)
