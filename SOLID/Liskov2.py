from abc import ABC, abstractmethod
# Base abstraction
class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass
# Intermediate abstraction that handles minimum amount logic
class MinimumAmountPayment(Payment):
    MIN_AMOUNT = 0
    def pay(self, amount: float):

        if amount < self.MIN_AMOUNT:
            raise ValueError(
                f"Amount must be at least {self.MIN_AMOUNT}"
            )

        self.process(amount)

    @abstractmethod
    def process(self, amount: float):
        pass
# Concrete payment types
class CardPayment(MinimumAmountPayment):

    MIN_AMOUNT = 1

    def process(self, amount: float):
        print(f"Card payment processed: {amount}")


class CryptoPayment(MinimumAmountPayment):

    MIN_AMOUNT = 1000

    def process(self, amount: float):
        print(f"Crypto payment processed: {amount}")


class UPIPayment(MinimumAmountPayment):

    MIN_AMOUNT = 10

    def process(self, amount: float):
        print(f"UPI payment processed: {amount}")


# Client code
def checkout(payment: Payment, amount: float):
    payment.pay(amount)

# Usage
card = CardPayment()
crypto = CryptoPayment()
upi = UPIPayment()

checkout(card, 50)
checkout(crypto, 1500)
checkout(upi, 20)