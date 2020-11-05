from src.payment.payment import Payment


class CreditCard(Payment):
    def __init__(self, methods):
        super().__init__()
        self.methods = methods
