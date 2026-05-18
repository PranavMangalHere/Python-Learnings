class Descripter:
    def __set_name__(self, owner, name):
        self.name = name 
    
    def __set__(self, instance, value):
        if self.name == "age" and value < 18:
            raise ValueError("Value must be greater than 10")
        instance.__dict__[self.name] = value
 
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

class Person:
    name = Descripter()
    age = Descripter()
    

p = Person()
p.name = "Pranav"
p.age = 23
print(p.name)
print(p.age)
p.age = 12
print(p.age)