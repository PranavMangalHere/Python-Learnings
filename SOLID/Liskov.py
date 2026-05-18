class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def set_width(self, w):
        self.width = w
        self.height = w

    def set_height(self, h):
        self.width = h
        self.height = h
        
def resize_rectangle(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(4)
    print(rect.area())
    
    
resize_rectangle(Rectangle(2, 3))
resize_rectangle()

""" Bad design """

# class Bird:
#     def fly(self):
#         print("Flying")


# class Ostrich(Bird):
#     def fly(self):
#         raise Exception("Ostrich can't fly")

# from abc import ABC, abstractmethod

# class Bird(ABC):
#     @abstractmethod
#     def fly(self):
#         pass

# class FlyingBird(Bird):
#     def fly(self):
#         print("can fly")

# class NonFlyingBird(Bird):
#     def fly(self):
#         raise Exception("no they can't")

# class Ostrich(NonFlyingBird):
#     def fly(self):
#         raise Exception("Ostrich can't fly")

# class sparrow(FlyingBird):
#     def fly(self):
#         print("sparrow can flyyyyy")
        
        
from abc import ABC, abstractmethod


class Bird(ABC):
    pass


class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass


class Sparrow(FlyingBird):

    def fly(self):
        print("Sparrow can fly")


class Ostrich(Bird):

    def run(self):
        print("Ostrich runs fast")
        

