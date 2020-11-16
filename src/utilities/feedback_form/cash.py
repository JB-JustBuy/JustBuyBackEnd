from src.utilities.feedback_form.feedback_form import FeedBackForm


class Cash(FeedBackForm):
    def __init__(self, amount=None, pct=None):
        super().__init__()
        self.amount = amount
        self.pct = pct

    def feedback(self, price=None):
        # sum of feedback from amount and percentage
        fd_amount = self.amount if self.amount else 0
        fd_pct = price * self.pct if self.pct else 0
        return fd_amount + fd_pct

