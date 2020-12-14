from src.entities.feedback_method.feedback_method import FeedBackMethod
import abc, logging
import numpy as np


class Payment(metaclass=abc.ABCMeta):
    def __init__(self):
        self.methods = []
        self.name = None
        self.type = None

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'methods': [method.to_dict() for method in self.methods]
        }

    def add_method(self, method):
        if isinstance(method, FeedBackMethod):
            self.methods.append(method)
        else:
            raise TypeError("Paras: 'method' is not FeedBackMethod!")

    def get_best_feedback_method(self, methods):
        feedback = [method.feedback() for method in methods]
        idx = np.argmax(feedback)
        return methods[idx]

    def get_qualified_best_method(self, merchandises):
        qualified_methods = []
        for method in self.methods:
            if method.qualify(merchandises):
                qualified_methods.append(method)

        return self.get_best_feedback_method(qualified_methods)

    def log(self, merchandises, qualified_methods):
        log = ""
        for merchandise in merchandises:
            log += merchandise.name
        logging.info("Merchandises, included {}".format(log), end='')

        if qualified_methods != []:
            logging('qualified methods have:')
            for method in qualified_methods:
                logging(method.to_dict())
        else:
            logging('cant find qualified methods')