import sys

# sys.argv[0] is always the name of the script (demo.py)
# sys.argv[1] would be "hello"
# sys.argv[2] would be "10"
# sys.argv[3] would be "True"

if len(sys.argv) > 3:
    name = sys.argv[1]
    count = int(sys.argv[2])    # Convert string to integer
    is_active = sys.argv[3] == "True"  # Convert string to boolean
    
    print(f"Name: {name}, Count: {count}, Active: {is_active}")
else:
    print("Please provide all three arguments.")

