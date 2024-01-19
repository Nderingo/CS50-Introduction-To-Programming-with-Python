with open("students.csv") as file:
    for line in file:
        name, house, years = line.rstrip().split(",")
        print(f"{name} is in {house} for {years}")