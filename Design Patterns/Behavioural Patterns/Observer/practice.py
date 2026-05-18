from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, product):
        pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []
        self.prev_price = price

    def attach(self, observer):
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        if self.price < self.prev_price:
            for observer in self.observers:
                observer.update(self)
    def set_price(self, price):
        self.prev_price = self.price
        self.price = price
        self.notify()

class EmailNotifier(Observer):
    def update(self, product):
        print(f"Mobile: Price dropped to {product.price}")

class MobileNotifier(Observer):
    def update(self, product):
        if product.price <= 500:
            print(f"Mobile: Price dropped to {product.price}")

class WhatsAppNotifier(Observer):
    def update(self, product):
        percentage = product.price / product.prev_price * 100
        if percentage > 20:
            print(f"WhatsApp Alert: {product.price}")

product = Product("iPhone", 1000)

mobile = MobileNotifier()
email = EmailNotifier()
whatsapp = WhatsAppNotifier()

product.attach(mobile)
product.attach(email)
product.attach(whatsapp)

product.set_price(900)   # all? maybe
product.set_price(850)   # conditional
product.set_price(600)
product.set_price(400)

product.detach(email)

product.set_price(300)