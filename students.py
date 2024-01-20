#with open("students.csv") as file:
#    for line in file:
#        name, house, years = line.rstrip().split(",")
#        print(f"{name} is in {house} for {years}")

#Alternatively
        
students = []

with open("students.csv") as file:
    for line in file:
        name,house,years = line.rstrip().split(",")
        students.append(f"{name} is in {house} for {years} years")
#Sortings
#for student in sorted(students):
#    print(student)
        student = {}
        student["name"] = name
        student["house"] = house
        student["years"] = years
        students.append(student)
        