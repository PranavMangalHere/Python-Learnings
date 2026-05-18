import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end)
        print(start)
    return wrapper

def hello():
    print("Hello World")
    time.sleep(2)

a = timer(hello)
a()