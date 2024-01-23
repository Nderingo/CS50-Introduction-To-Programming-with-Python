#with open("students.csv") as file:
#    for line in file:
#        name, house, years = line.rstrip().split(",")
#        print(f"{name} is in {house} for {years}")

#Alternatively
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name: row[0]"}, "home: row[1]")
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        students.append(student)


for student in sorted(students, key = lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")



#Sortings
#for student in sorted(students):
#    print(student)
        
#       students.append(student)

