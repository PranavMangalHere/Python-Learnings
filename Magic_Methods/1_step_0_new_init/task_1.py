"""class Student:
    def __new__(cls, *args, **kwargs):
        print("Creating Student Object")
        return super().__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("student initialized")
        

s = Student("pranav", 43)"""


class Singleton:
    _cls_instance = None
    
    def __new__(cls):
        if cls._cls_instance is None:
            print("creating new instance")
            cls._cls_instance = super().__new__(cls)
        return cls._cls_instance

a = Singleton()
b = Singleton()

print(a is b)

     