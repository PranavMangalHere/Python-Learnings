# Step 1 — Create Component (Base Class)
class Coffee:
    def cost(self):
        return 50

#Step 2 — Create Base Decorator(This decorator holds the original object.)
class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost()

# milk decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 10

# sugar decorator
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 5

coffee = Coffee()

coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())










"""
I have one question in both the cases we have done inheritance and have same no. of classes then 
how does it solves the problem
"""
"""
You are right that both examples use inheritance and have similar number of classes,
but the real difference is not the number of classes — it is how objects are combined."""

"""
3️⃣ Key Difference
❌ Without Decorator

Combination is hardcoded in classes
CoffeeWithMilkAndSugar
CoffeeWithMilkAndHoney
CoffeeWithMilkSugarHoney
Each new combination → new class
"""

## so it avoids class explosion by allowing behavior to be added dynamically through object composition
# instead of creating subclasses for every feature combination.