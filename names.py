#names = []

#for _ in range(3):
#    names.append(input("What is your name? "))
    
#for name in sorted(names):
#    print(f"hello, {name}")

name = input("What is your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()