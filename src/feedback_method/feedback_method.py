from src.feedback_constraint.single_full import SingleFull

class FeedBackMethod(object):
    def __init__(self, constraint, form):
        self.constraint = constraint
        self.form = form

    def trigger(self, merchandises):
        if self.is_satisfied(merchandises):
            print("constraint is single full and constraint is satisfied")
            return self.feedback(merchandises)
        else:
            return False

    def is_satisfied(self, merchandises):
        return self.constraint.is_satisfied(merchandises)

    #***
    def feedback(self, merchandises):
        if isinstance(self.constraint, SingleFull):
            price = self.constraint.amount
            return self.form.feedback(price)

