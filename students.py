#with open("students.csv") as file:
#    for line in file:
#        name, house, years = line.rstrip().split(",")
#        print(f"{name} is in {house} for {years}")

#Alternatively
        
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_student(student):
    return student["name"]

for student in sorted(students, key=get_student, reverse=True):
    print(f"{student['name']} is in {student['house']}")



#Sortings
#for student in sorted(students):
#    print(student)
        
#       students.append(student)

