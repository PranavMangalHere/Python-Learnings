from functools import reduce

lst = ["1", "2", "3", "4"]
result = list(map(lambda x:int(x) , lst))
print(result)

lst = [1,2,3,4,5,6,7]
result = list(filter( lambda x:x%2!=0 , lst))
print(result)

lst = [1,2,3,4]
result = reduce( lambda x,y:x*y, lst)
print(result)

lst = [0, 20, 37, 100]
result =list(map( lambda x: (9/5)*x + 32 , lst))
print(result)

words = ["apple", "sky", "orange", "try"]
result = list(filter( lambda w : not any( char in "aeiou" for char in w ) , words))
print(result)

lst = [10, 55, 3, 99, 23]
result = reduce( lambda x,y : x if x>y else y , lst )
print(result)


lst = [1,2,3,4,5,6,7,8]

result = reduce( lambda x,y : x+y ,
    list(map(
    lambda x:x**2 ,
    list(filter( lambda x:x%2==0 , lst))
    )))
print(result)

a = [1,2,3]
b = [10,20,30]

result = list(map( lambda x,y:x+y ,a,b))
print(result)

s = 5
result = reduce( lambda x,y:x*y , range(1, s+1))
print(result)