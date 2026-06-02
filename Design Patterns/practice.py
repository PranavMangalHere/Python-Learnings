from abc import ABC, abstractmethod


class Car(ABC):
    
    @abstractmethod
    def drive(self):
        pass
    
class Sedan(Car):
    def drive(self):
        print("Driving sedan")

class Suv(Car):
    def drive(self):
        print("Driving SUV")

class Factory:
    
    @staticmethod
    def give_car(val):
        if val == 'Sedan':
            car = Sedan()
            return car
        elif val == 'Suv':
            car = Suv()
            return car
        else:
            raise ValueError(" enter valid car ")

c = Factory.give_car("Sedan")
c.drive()

# c2 = Factory.give_car("sd")
# c2.drive()
print("------------------------------------------------")
class Pizza :
    
    def __init__(self):
        self._base = "regular"
        self._toppings = []
        self._cheese = False
        
    def base(self, base):
        if base in ["Regular", "Medium", "Large"]:
            self._base = base
        return self
    def toppings(self, lst):
        self._toppings.extend(lst)
        return self
    def cheese(self, choice = 'No'):
        if choice == 'Yes':
            self._cheese = True
        return self
    
    def build(self):
        print("make your pizza")
        return {
            "base":self._base,
            "toppings":self._toppings,
            "cheese":self._cheese
        }

p = Pizza().base("Large").toppings(["olive", 'mushroom']).cheese('Yes').build()
print(p)
print("------------------------------------------------")


class Singleton:
    _instance =None
    def __new__(cls):
        if cls._instance is None:
            print("new object created")
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        print("Initialized")
obj1 = Singleton()
obj2 = Singleton()

print("------------------------------------------------")
# import requests
""" 
Question 3 (Very Frequently Asked in API Automation Interviews)
You receive the following API response:
{
    "page": 1,
    "total": 3,
    "users": [
        {
            "id": 1,
            "name": "John"
        },
        {
            "id": 2,
            "name": "Alice"
        },
        {
            "id": 3,
            "name": "Bob"
        }
    ]
}
Task
Write a function that validates:
Status code is 200
total field matches the actual number of users
Every user has id and name
IDs are unique
IDs are positive integers
At least one user exists
"""

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass
class PaypalPayment(PaymentStrategy):
    def pay(self):
        print("payment using Paypal")
class UPIPayment(PaymentStrategy):
    def pay(self):
        print("payment using UPI")
class CreditPayment(PaymentStrategy):
    def pay(self):
        print("payment using CreditCard")

class PaymentProcesser:
    def __init__(self, strategy : PaymentStrategy):
        self.strategy = strategy
        
    def pay(self):
        self.strategy.pay()
    
pay = PaymentProcesser(UPIPayment())
pay.pay()

print("------------------------------------------------")

class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass

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
            print("notify")
            observer.update(self.price)
    
    def set_price(self, price):
        self.price = price
        self.notify()

class Emailnotify(Observer):
    def update(self, price):
        print(f"email of price drop {price} less")
class MoblieAPPnotify(Observer):
    def update(self, price):
        print(f"APP notification of price drop {price} less")
class TVnotify(Observer):
    def update(self, price):
        print(f"SMS of price drop {price} less")

email = Emailnotify()
mobile = MoblieAPPnotify()
tv = TVnotify()

s = Stock()

s.attach(email)
s.attach(mobile)
s.attach(tv)

s.set_price(123)