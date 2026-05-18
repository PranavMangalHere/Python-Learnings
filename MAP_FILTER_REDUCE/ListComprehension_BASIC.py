from functools import reduce
# Create a list of squares from 1 to 10 using list comprehension.
lst = [i**2 for i in range(1, 11)]
print(lst)
print("------------------------------------")

# Convert a list of strings to uppercase using list comprehension.
lst = ['bvhb', "jhb","jhbhjb"]
res = [i.upper() for i in lst ]
print(res)
print("------------------------------------")

# Extract only even numbers from a list.
lst = [1,3,5,6,7,8,8,3,2,1]
res = [i for i in lst if i%2 == 0 ]
print(res)
print("------------------------------------")

# Create a list of lengths of words in a sentence.
sentence = "tyt yugug guyg hggjh"
lst = sentence.split()
res = [len(i) for i in lst ]
print(res)
print("------------------------------------")

# Replace negative numbers with 0 in a list.
lst = [1,3,4,5,-1,5,-1,-1]
res = [ i if i>0 else 0 for i in lst ] 
print(res)
print("------------------------------------")

# Use map() to convert a list of strings into integers.
lst = ["12", "32"]
res = list(map(lambda x:int(x) , lst))
print(res)
print("------------------------------------")

# Use map() to calculate squares of numbers.
lst = [3, 5, 4, 5]
res = list(map(lambda x:x**2, lst))
print(res)
print("------------------------------------")

# Convert temperatures from Celsius to Fahrenheit using map().
lst = [3, 5, 4, 5]
res = list(map(lambda x:(x*(9/5)) + 32, lst))
print(res)
print("------------------------------------")

# Filter even numbers from a list.
lst = [1,3,5,6,7,8,8,3,2,1]
res = list(filter(lambda x:x%2==0, lst))
print(res)
print("------------------------------------")

# Filter non-empty strings from a list.
lst = ["hi", "", "hello", ""]
res = list(filter(lambda x:len(x)>0 , lst)) 
print(res)
print("------------------------------------")


# Find sum of numbers using reduce()
lst = [1,3,5,6,7,8,8,3,2,1]
res = reduce(lambda a,b: a+b , lst)
print(res)
print("------------------------------------")

# Find maximum number using reduce()
lst = [1,3,5,6,7,8,8,3,2,1]
res = reduce(lambda a,b:max(a,b) , lst)
print(res)
print("------------------------------------")

