from src.utilities.feedback_constraint.single_full import SingleFull
from src.utilities.feedback_constraint.quantity_enough import QuantityEnough

class FeedBackMethod(object):
    def __init__(self, constraint, form):
        self.constraint = constraint
        self.form = form

    def trigger(self, merchandises):
        if self.qualify(merchandises):
            print("constraint is single full and constraint is satisfied")
            return self.feedback(merchandises)
        else:
            return False

    def qualify(self, merchandises):
        return self.constraint.qualify(merchandises)

    #***
    def feedback(self, merchandises=None):
        if isinstance(self.constraint, SingleFull):
            price = self.constraint.amount
            return self.form.feedback(price)
        elif isinstance(self.constraint, QuantityEnough):
            return self.form.feedback()
