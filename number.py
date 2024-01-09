while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    # Use of else statementto solve the NameError
    else:
        break

print(f"x is {x}")