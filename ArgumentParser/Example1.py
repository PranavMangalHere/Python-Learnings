import argparse
"""parser = argparse.ArgumentParser(description ='Process some integers.')
parser.add_argument('integers', metavar ='N',
                    type = int, nargs ='+',
                    help ='an integer for the accumulator')

parser.add_argument('--sum', dest ='accumulate',
                    action ='store_const',
                    const = sum,
                    help ='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))"""

""" 
2 Types of arguments 
Positional , optional arguments
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="sum the integers")
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
    else :
        print(n1 * n2)