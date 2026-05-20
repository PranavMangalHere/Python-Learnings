"""
1. Simple Generator
Create a generator that yields numbers from 1 to n.
Example:
gen = numbers(5)
# Output:
1 2 3 4 5
"""

def numbers(nums):
    for i in range(1, nums+1):
        yield i
# gen = list(numbers(5))
# print(gen)

""" 
2. Even Number Generator
Create a generator that yields only even numbers between 1 and n.
Example:
2 4 6 8
"""

def even_numbers(nums):
    for i in range(1, nums+1):
        if i%2 == 0:
            yield i
# even = list(even_numbers(10))
# print(even)

""" 
3. Reverse String Generator
Create a generator that yields characters of a string in reverse order.
Example:
"hello"
# Output:
o l l e h
"""

def reverse_str(string):
    n = len(string)
    for i in range(len(string)):
        yield string[n-i-1]

# result = list(reverse_str("hello"))
# print(result)

""" 
4. Square Generator
Create a generator that yields squares of numbers from 1 to n.
Example:
1 4 9 16 25
"""

def sq_gen(nums):
    for i in range(1, nums+1):
        yield i**2

# result = list(sq_gen(10))
# print(result)

""" 
5. Fibonacci Generator
Create a Fibonacci generator that yields first n Fibonacci numbers.
Example:
0 1 1 2 3 5 8
"""

def fibo(nums):
    a = 0
    b = 1
    for i in range( nums):
        yield a
        a, b = b, a+b

# result = list(fibo(10))
# print(result)
