import logging

logging.basicConfig(filename = 'ex2.log',
                    filemode = 'a',
                    level = logging.DEBUG,
                    format= "%(process)s: %(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    )

# try :
#     age = int(input("Enter your age: "))
#     logging.info(f"Your age is: {age}")
# except Exception as e:
#     logging.exception(e)

class AccessDenied(Exception):
    pass

try :
    age = int(input("Enter your age: "))
    if age < 18:
        raise AccessDenied("Access Denied")
    logging.info(f"You are {age} years old")
except Exception as e:
    logging.exception(e)