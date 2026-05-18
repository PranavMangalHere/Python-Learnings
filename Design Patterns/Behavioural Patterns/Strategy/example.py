## Solution using strategy pattern

# Step 1: Create Strategy Interface
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Create Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Credit card payment {amount}")
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"PayPal payment {amount}")
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"UPI payment {amount}")

# Step 3: Context Class

class PaymentProcessor:
    def __init__(self, strategy : PaymentStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy : PaymentStrategy):
        self.strategy = strategy
    def pay(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(PayPalPayment())
processor.pay(3000)