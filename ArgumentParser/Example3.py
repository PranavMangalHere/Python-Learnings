import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number",  nargs = '+', type = int, help="number")
parser.add_argument('operation', choices=["sorted"])

args = parser.parse_args()

print(args.number)

operations = {
    "sorted": sorted
}


print(operations[args.operation](args.number))