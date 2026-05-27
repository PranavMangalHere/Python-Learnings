from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


class Sedan(Car):
    def drive(self):
        print("Driving a Sedan")


class SUV(Car):
    def drive(self):
        print("Driving an SUV")


class CarFactory:
    def create_car(self, car_type: str) -> Car:
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Unknown car type")


factory = CarFactory()

car1 = factory.create_car("sedan")
car2 = factory.create_car("suv")

car1.drive()
car2.drive()
