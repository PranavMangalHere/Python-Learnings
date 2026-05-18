def sanity_check(*data_Type):
    def outer_wrap(func):
        def inner_wrap(*args):
            if isinstance(args[0] , data_Type) :
                func(*args)
            else:
                raise TypeError("Integer daal naa ...")
        return inner_wrap
    return outer_wrap

@sanity_check(int, float)
def square(num):
    print(num**2)

square(3.4)