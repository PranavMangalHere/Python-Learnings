# class Number:
#     def __init__(self, value):
#         self.value = value
        
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return self.value + other.value
        
#         return NotImplemented
    
#     def __radd__(self, other):
#         return self.value + other

# n1 = Number(3)
# n2 = Number(4)

# print(n1 + n2)

# print(10+n1)


class Vector:
    
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        
    def __add__(self, other):
        val1 = self.v1 + other.v1
        val2 = self.v2 + other.v2
        return f"({val1}, {val2})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2 
print(v3)