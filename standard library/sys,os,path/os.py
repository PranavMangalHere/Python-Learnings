import os
# print(dir(os))

## Wroking with the current directory
# print(os.getcwd())
# os.chdir(r"C:\\Users\\PranavMangal\Desktop\\Python my work deep dive")
# print(os.getcwd())


## file and directory Management

# os.mkdir("newfolder")
# os.makedirs("demo1/demo2")
# os.rmdir("newfolder")
# os.removedirs("demo1/demo2")

# print(os.listdir())

# var = os.walk(os.getcwd()) # tuples ki form mai puran data deta hai 
# # print(var)

# for value in var:
#     print(value)

# stats = os.stat('./os.py')
# print(stats.st_size)

# os.path.basename('')
# os.path.dirname('')
# print(os.path.exists("./temp/abc.txt"))

# if os.path.exists('newfolder/onefolder'):
#     os.mkdir('newfolder/onefolder')
# else:
#     print('folder does not exist')

# path = os.path.join("C:", "Users", "PranavMangal", "Desktop")
# print(path)

# print(os.path.join("C:/Users", "D:/data", "file.txt")) # If any part is an absolute path, everything before it is discarded.

# print(os.path.abspath("os.py")) #Converts a relative path → absolute path.

## Envirnment Variables - depends on os to os 

# print(os.system('dir'))

# print(os.getenv('PATH'))  # reads environment variables from the operating system.

