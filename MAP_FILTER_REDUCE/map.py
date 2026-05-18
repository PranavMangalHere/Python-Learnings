"""✅ Mini Tasks (Try Yourself)
Task 1

Square only even numbers from list
👉 Use all 3 (map + filter + reduce)

Task 2 (Interview Level)

Find maximum even number after squaring odd numbers"""

from functools import reduce

lst = [1,2,3,4,5,6,7,8]
result = reduce( 
    lambda a, b : a if a>b else b ,
    list(map(
    lambda x:x*x,
    list(filter(lambda x:x%2 == 0 , lst)))))

print(result)