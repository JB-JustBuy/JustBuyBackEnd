from src.entities.payment.payment import Payment


class CreditCard(Payment):
    def __init__(self, name, belong_to=None):
        super().__init__()
        self.belong_to = belong_to
        self.name = name
        self.type = "Credit Card"
