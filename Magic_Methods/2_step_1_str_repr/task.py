class car:
    def __init__(self):
        self.brand = "BMW"
        self.price = 5000000
    
    def __str__(self):
        return f"Car: {self.brand} costs {self.price}"
    
    def __repr__(self):
        return f"Car('{self.brand}', {self.price} )"

c = car()
print(c)
c

