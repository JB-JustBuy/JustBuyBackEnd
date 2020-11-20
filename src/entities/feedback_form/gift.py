from src.entities.feedback_form.feedback_form import FeedBackForm
from src.entities.merchandise.merchandise import Merchandise


class Gift(FeedBackForm):
    def __init__(self, merchandise):
        super().__init__()
        if not isinstance(merchandise, Merchandise):
            raise TypeError("Gift paras need to <Merchandise>")
        self.md = merchandise

    def feedback(self, price=None):
        return self.md.price * self.md.quantity
