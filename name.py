import sys

#Check for Errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")

# For multiple arguments
for arg in sys.argv[1:-2]:

# Print name tags
#    print("Hello, my name is", sys.argv[1])
    print("Hello, my name is", arg)