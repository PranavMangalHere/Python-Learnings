""" 
Medium Level
6. Prime Number Generator
Create a generator that yields prime numbers up to n.
Example:
2 3 5 7 11 13
"""

def prime_num(nums):
    
    for num in range(2,nums+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1 ):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# result = list(prime_num(10))
# print(result)

""" 
7. File Line Generator
Create a generator function that reads a text file line by line using yield.
Goal:
Do not use readlines()
Memory efficient reading
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(BASE_DIR, "abc.txt")

def file_reader(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line

# result = list(file_reader(full_path))
# print(result)

""" 
8. Countdown Generator
Create a generator that counts down from n to 0.
Extra:
Print "Blast Off" after completion.
Example:
5 4 3 2 1 0 Blast Off
"""

def countdown(n):
    while n >= 0:
        yield n
        n -= 1
    return "Blast Off"
gen = countdown(5)

try:
    while True:
        print(next(gen), end=" ")
except StopIteration as e:
    print(e.value)


""" 
9. Generator Expression Problem
Using generator expression:
Generate cubes of numbers from 1-20
Print only numbers divisible by 5
"""

result = ( i**3 for i in range(1,20+1) if i%5 == 0 ) 
print(tuple(result))


""" 
10. Custom range() Generator
Create your own version of Python's range() using generators.
Support:
my_range(start, stop, step)
Example:
list(my_range(1, 10, 2))
# Output:
[1, 3, 5, 7, 9]
"""

def my_range(start, stop = None, step = 1):
    
    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError("step cannot be 0")
    
    if step  > 0:
        while(start<stop):
            yield start
            start = start + step
    else:
        while start > stop:
            yield start
            start += step

# print(list(my_range(1, 10, 2)))
# result = list(my_range(10, 0, -2))
# print(result)