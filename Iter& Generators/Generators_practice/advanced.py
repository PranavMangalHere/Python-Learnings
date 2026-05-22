""" 
11. Infinite Generator
Create an infinite generator for natural numbers.
Example:
1 2 3 4 5 ...
Use next() to fetch values.
"""

def inf_gen():
    i = 1
    while True:
        yield i
        i += 1
gen = inf_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

""" 
12. Generator Pipeline
Given:
nums = [1,2,3,4,5,6,7,8,9,10]
Create generator pipeline:
Filter even numbers
Square them
Yield results lazily
Expected:
4 16 36 64 100
"""
nums = [1,2,3,4,5,6,7,8,9,10]
def even_nums(nums):
    
    for num in nums:
        if num%2 == 0:
            yield num

def square_nums(nums):
    for num in nums:
        yield num**2

res = square_nums(list(even_nums(nums)))

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

""" 
13. Flatten Nested List Generator
Flatten nested lists using generators.
Example:
[1, [2,3], [4,[5,6]], 7]
Output:
1 2 3 4 5 6 7
(Hint: recursion + yield from)
"""
lst = [1, [2,3], [4,[5,6]], 7]
def flatten(lst):
    for element in lst:
        
        if isinstance(element, list):
            yield from flatten(element)
            
        else :
            yield element

res = list(flatten(lst))
# print(res)

""" 
14. yield from Problem
Create two generators:
gen1()
gen2()
Then combine them using:
yield from
Expected:
1 2 3 a b c
"""

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield 'a'
    yield 'b'
    yield 'c'

def combined():
    yield from gen1()
    yield from gen2()

res = list(combined())
print(res)

""" 
15. Coroutine Generator (send())
Create a generator that:
starts with value 0
accepts values using .send()
keeps adding them
yields running total
Example:
g = accumulator()
next(g)
g.send(10) -> 10
g.send(5)  -> 15
g.send(20) -> 35
"""

def accumulator():
    
    total = 0 
    
    while True:
        value = yield total
        
        total = total + value

g = accumulator()

# print(next(g))
# print(g.send(10))
# print(g.send(10))
# print(g.send(10))

 
a = [1,2,3]
b = ['a','b','c']
c = [10,20,30,40]

def round_robin(*args):
    
    iterators = [iter(i) for i in args]
    
    while iterators:
        
        for it in iterators:
            
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)

result = list(round_robin(a, b, c))

print(result)    
    