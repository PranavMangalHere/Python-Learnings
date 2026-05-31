def dec(func):
    def wrapper(s1,s2):
        try:
            return func(s1,s2)
        except AssertionError as e:
            print("Error")
    return wrapper

@dec
def match(s1,s2):
    assert s1==s2
match("hi", "hye")
match("hi","hi")
 