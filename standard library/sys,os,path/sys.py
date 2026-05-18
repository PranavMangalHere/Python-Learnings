import sys
# it interacts with python interpreter

# import math
# print(type(sys.argv)) # list 
# # ek argument toh milega hi milega jo hamesha file ka naam hota hai current file ka 
# print("size of argv", len(sys.argv))
# print(sys.argv)
# print(sys.argv[3])


# print(len(sys.modules)) # dictionary mai store hota hai 

# 
# print(sys.maxsize) # 9223372036854775807
# my_list = list(range(sys.maxsize+ 1))

# print(sys.version) # info of python interpretor you are running
# print(sys.version_info)

# print(sys.platform)

# stdin - input read karne ke liye 
# stdout- output read karne ke liye 
# stderr- err aa rahi hai

# for words in sys.stdin:
#     if 'quit' == words.strip():
#         break
#     print(f"Input : {words}")
# print("Exit!")

# sys.stdout = open('output.txt', 'w')
# sys.stderr = open('error.txt', 'w')

# print("this is the standard output")

# try:
#     1/0
# except ZeroDivisionError as e:
#     print(f"Error occured {e}", file = sys.stderr)
    
# sys.stdout.close()
# sys.stderr.close()

# Exit the program - sys.exit()
# size of an object in byte - sys.getsizeof()
# Recursion limit - sys.getrecursionlimit(), sys.setrecursionlimit(limit)
# print(sys.getrecursionlimit()) # 1000
# print(sys.exit("Custom message"))
# a = 10
# print(sys.getsizeof(a)) #28

# sys.setrecursionlimit(1100)
# def rec(n):
#     print(n)
#     rec(n+1)

# rec(1)

# python checks roughly every 0.005 seconds wether it should switch to another thread
# print(sys.getswitchinterval())
# print(sys.setswitchinterval(.03))
# print(sys.getswitchinterval())

# print(sys.getwindowsversion())

"""
    When to use sys module 
-> command- line scripts: sys.argv
-> program termination- to exit the script with a specfic status code or message sys.exit(0)
-> custom I/O management- to control how input, output or error strams are handled
-> Environment management- To manupilate the python module search path (sys.path)
-> Debugging and logging: to customize how exceptions are handled
(sys.excepthook)
"""

