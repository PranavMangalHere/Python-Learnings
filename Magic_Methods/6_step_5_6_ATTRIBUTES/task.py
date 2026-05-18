# class A:
    
#     def __setattr__(self, name, value):
#         print(f"Object value is set{name} = {value}")
#         super().__setattr__(name, value)
    
#     def __getattribute__(self, name):
#         return super().__getattribute__(name)
    
# a = A()
# a.d = 9
# print(a.d)


class User:
    def __setattr__(self, name, value):
        if name == 'age' and value >= 18:
            print(f"set{name}= {value}")
            super().__setattr__(name, value)
        else:
            raise ValueError
        
u = User()
u.age = 32