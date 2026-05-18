class Coffee:
    def cost(self):
        return 50
class CoffeeWithMilk(Coffee):
    def cost(self):
        return 50 + 10


class CoffeeWithSugar(Coffee):
    def cost(self):
        return 50 + 5


class CoffeeWithMilkAndSugar(Coffee):
    def cost(self):
        return 50 + 10 + 5


coffee = CoffeeWithMilkAndSugar()
print(coffee.cost())