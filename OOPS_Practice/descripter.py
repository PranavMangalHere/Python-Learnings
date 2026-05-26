class EmailDescripter():
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
    
    def __set__(self,instance, value):
        if ".com" not in value or "@" not in value:
            raise ValueError("Enter valid email")
        
        instance.__dict__[self.name] = value

class Email:
    
    email = EmailDescripter()
    
    def __init__(self, email):
        self.email = email
        

e = Email("pranav@gmail.com")
print(e.email)
e.email = "ertyui@gmail.com"
print(e.email)