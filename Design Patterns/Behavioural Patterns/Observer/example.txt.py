# Step 1: Observer Interface
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass

# Step 2: Subject
class Stock:
    def __init__(self):
        self.observers = []
        self.price = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.price)

    def set_price(self, price):
        self.price = price
        self.notify()

# Step 3: Concrete Observers

class MobileApp(Observer):
    def update(self, price):
        print(f"📱 Mobile App: Stock price updated to {price}")

class EmailService(Observer):
    def update(self, price):
        print(f"📧 Email: Stock price updated to {price}")

class TVDisplay(Observer):
    def update(self, price):
        print(f"📺 TV: Stock price updated to {price}")


stock = Stock()

mobile = MobileApp()
email = EmailService()
tv = TVDisplay()

stock.attach(mobile)
stock.attach(email)
stock.attach(tv)

stock.set_price(100)
stock.set_price(120)