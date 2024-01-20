#with open("students.csv") as file:
#    for line in file:
#        name, house, years = line.rstrip().split(",")
#        print(f"{name} is in {house} for {years}")

#Alternatively
        
students = []

with open("students.csv") as file:
    for line in file:
        names,house,years = line.rstrip().split(",")
        students.append(f"{names} is in {house} for {years}")

for student in sorted(students):
    print(student)