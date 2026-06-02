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


# 3. Create Cartesian Product
a = [1,2,3]
b = ['x','y']
res = [(num, num2) for num in a for num2 in b]
print(res)
print("------------------------------------")


# 6. Multiple Conditions
# Return words:
# length > 3
# starts with vowel
words = ["apple", "dog", "orange", "cat", "elephant", "dfgh"]
res = [i for i in words if len(i) > 3 and i.strip()[0] in "aeiou"]
print(res)
print("------------------------------------")

# 9. Split Sentences Into Words
sentences = [
    "python is awesome",
    "list comprehension rocks",
    " guygy huguy ", 
    " "
]
res = [word for words in sentences for word in words.strip().split(" ") if len(word) > 0]
print(res)
print("------------------------------------")

# 10. Find Palindromes
words = ["madam", "apple", "racecar", "python"]
res = [word for word in words if word == word[::-1]]
print(res)
print("------------------------------------")


# 12. Build Dictionary From Two Lists
keys = ["id", "name", "age"]
values = [101, "Pranav", 22]
res = {k:v for k, v in zip(keys, values)}
print(res)


# arr = [1,2,[1,2],(3,4), "qwer"]
# result = [i 
# for lst in arr
# for i in ( lst if isinstance(lst, (list, tuple)) else ( list(lst) if isinstance(lst, str) else [lst] ) )
# ]
# print(result)
# colors = ["red", "blue"]
# sizes = ["S", "M", "L"]

# result = [ (c, s)
#     for c in colors
#     for s in sizes
#     ]
# print(result)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# rows = len(matrix)
# cols = len(matrix[0])

# result =[
#     [matrix[row][col] for row in range(rows)]
#     for col in range(cols)
#     ]
# print(result)

# sentence = "python is powerful and python is fun"

# seen = set()
# result=[len(word) for word in sentence.split() if len(word) not in seen and not seen.add(len(word))]
# print(result)


# nums = 100
# result=[num for num in range(2,nums) if all(num%i != 0 for i in range(2,int(num**0.5)+1))]
# print(result)


# text = "apple banana apple mango banana apple"
# result = {
#     word : sum(1 for x in text.split(" ") if word == x )
#     for word in text.split(" ")
# }
# print(result)
