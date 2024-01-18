names = []

#for _ in range(3):
#    names.append(input("What is your name? "))
    
#for name in sorted(names):
#    print(f"hello, {name}")

# Writing the names to the file
#name = input("What is your name? ")

#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

#Read the names from the file
    
with open("names.txt") as file:
    for line in file:
       names.append(line.rstrip())


for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#Alternatively to read and sort a file
#with open("names.txt") as file:
#    for line in sorted(file):
#       print("hello,", line.rstrip())
