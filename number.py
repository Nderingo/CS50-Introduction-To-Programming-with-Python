try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
# Use of else statementto solve the NameError
else:
    print(f"x is {x}")