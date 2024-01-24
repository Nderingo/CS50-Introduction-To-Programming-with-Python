import csv

name = input("What is your name? ")
home = input("Where is your home? ")

#with open("kids.csv", "a") as file:
 #   writer = csv.writer(file)
#    writer.writerow([name, home])

#Alternatively
with open("kids.csv", "a") as file:
    writer = csv.DictWriter(file,fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})

