# List Comprehension (Advanced)
# Transpose a matrix
# Example:
# 2x3 → 3x2
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [ [row[i] for row in matrix] for i in range(len(matrix[0])) ]
print(result)
print("------------------------------------------------")

# Remove duplicates from list while preserving order
# Example: [1,2,2,3,4,4] Expected: [1,2,3,4]
# list comprehension
lst = [1,2,2,3,4,4]
seen = set()
res = [x for x in lst if not (x in seen or seen.add(x))]
print(res)
print("------------------------------------------------")

# Nested conditional list comprehension
# Example:
# even → square
# odd → cube
lst = [1,2,3,4,5,6,7,8]
res = [x**2 if x%2 == 0 else x**3 for x in lst]
print(res)
print("------------------------------------------------")

# map() Advanced
# Apply function returning tuple
# Example:
# return (number, square)
res = list(map(lambda x:(x,x**2) , range(1,5)))
print(res)
print("------------------------------------------------")

# Filter words longer than average word length
# Example:
lst = ["apple","bat","banana"]
avg_len = sum(len(word) for word in lst)/ len(lst)
print(avg_len)
res = list(filter(lambda x:len(x) > avg_len , lst))
print(res)
print("------------------------------------------------")