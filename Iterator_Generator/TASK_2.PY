def merge_elems(*elems):
    for element in elems:
        if isinstance(element, str):
            for char in element:
                yield char
            continue
        
        try:
            for e in element:
                yield from merge_elems(e)
        except:
            yield element

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

# for x in merge_elems(a, b, c, d):
#     print(x, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

def map_like(fun, *elems):
    for element in elems:
        try :
            yield fun(element) 
        except:
            yield  f"{element}: {type(element)} object is not subscriptable"
            

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
    print(_)
    
# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable
