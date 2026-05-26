class User:
    def __new__(cls):
        print("Allocating memory")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializing object")

u = User()

""" 
Task 2 — Singleton Pattern
Allow only ONE object creation.
Example:
a = Database()
b = Database()
print(a is b)
Output:
True
Concepts:
class variable
object caching
overriding __new__
"""

class Database:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            print("Object creating")
            cls.instance = super().__new__(cls)
        return cls.instance
    
d1 = Database()
d2 = Database()

print(d1 is d2)


""" 
Interview-Level Task
Build mini ORM model:
class User(Model):
    pass
Requirements:
every object gets auto-generated ID
track all created objects
prevent duplicate IDs
store registry at class level
Use both:
__new____init__
properly.
"""

class Model:
    
    def __new__(cls, *args, **kwargs):
        obj  = super().__new__(cls)
        
        # obj.id = 