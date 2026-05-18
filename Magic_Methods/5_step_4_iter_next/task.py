# class ReverseList:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(self.data) - 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration
        
#         val = self.data[self.index]
#         self.index -= 1
#         return val

# r = ReverseList([1,2,4,5])
# for i in r:
#     print(i, end=" ")
    

class A:
    def __iter__(self):
        return [1,2,3]

a = A()

for x in a:
    print(x)
