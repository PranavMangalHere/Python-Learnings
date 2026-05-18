import argparse
from random import choices

## optional arguments (--arguments)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="sum the integers", choices = ['add', 'subtract', 'multiply', 'divide'])
    args = parser.parse_args()

    ## the arguments that we get are of string type
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)

    if args.operation == "add":
        print(n1 + n2)
    elif args.operation == "subtract":
        print(n1 - n2)
    elif args.operation == "multiply" :
        print(n1 * n2)
    elif args.operation == "divide":
        print(n1 / n2)
    else:
        print("Invalid operation")