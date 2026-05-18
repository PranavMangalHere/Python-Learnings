from functools import reduce 

# Flatten a nested list
lst = [[1,2],[3,4],(5,6), 7]
res = [i for ind in lst for i in (ind if isinstance(ind, (list, tuple)) else [ind])]
print(res)
print("----------------------------------------")

# Create a dictionary using list comprehension - sqaured mapping 
res = {i:i**2 for i in range(1,5)}
print(res)
print("----------------------------------------")

# Extract vowels from a string
str = "pythonic code"
res = [char for char in str if char in "aeiou"]
print(res)
print("----------------------------------------")

# Generate Cartesian product
# Example:
# [1,2] and ['a','b']
# Expected:
# [(1,'a'),(1,'b'),(2,'a'),(2,'b')]
lst = [1,2]
lst2 = ['a', 'b']
res = [ (ind, tup) for ind in lst for tup in lst2]
print(res)
print("----------------------------------------")

# map() (Intermediate)
# Apply a function to multiple iterables
# Example:
a=[1,2,3]
b=[4,5,6]
# Add both lists element-wise using map().
res = list(map(lambda x,y:x+y, a,b))
print(res)
print("----------------------------------------")

# Extract last character of each word
# Example:
# ["cat","dog"]
# Expected:
# ['t','g']
lst = ["cat","dog"]
res = list(map(lambda x:x[len(x)-1], lst))
print(res)
print("----------------------------------------")

# Filter prime numbers from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(filter( lambda n:n>1 and all(n%i != 0 for i in range(2, int(n**0.5)+1)) , lst))
print(res)
print("----------------------------------------")

# Filter palindromes from a list
lst = ["madam", "dfsvx","hello","racecar", "dsffv"]
res = list(filter(
    lambda word: word == word[::-1], lst
))
res = list( word for word in lst if word == word[::-1])
print(res)
print("----------------------------------------")

# Find factorial using reduce
n = 5
fact = reduce(lambda x,y: x*y , range(1, n+1))
print(fact)
print("----------------------------------------")

# Find longest string in list using reduce
lst = ["madam", "dfsvx","hello","racecar", "dsffv"]
res = reduce(lambda x,y:x if len(x) > len(y) else y , lst)
print(res)
print("----------------------------------------")

# Multiply only even numbers using reduce
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = reduce(
    lambda x, y: x*y ,
    list(filter(lambda x: x%2 == 0 , lst))
)
print(res)
print("----------------------------------------")

