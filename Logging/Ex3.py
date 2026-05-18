"""
Creating a logger decorator for a function
"""
import logging
def log(func):

    def wrapper(*args, **kwargs):
        logging.basicConfig(filename="Ex3.log",
                            level=logging.INFO,
                            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        logging.info(f"Function Name: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Function Result: {result}")
        return result
    return wrapper

@log
def double_func(a):

    return a*2

double_func(10)