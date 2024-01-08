#i =5
#while i != 0:
#   print("meow")
#   i = i-1

#While loops
#i = 0
#while i < 3:
#    print("meow")
#    i += 1

#FOR loops
#for i in range(19):
#   print("meow")

#while True:
#    n = int(input("What's n? "))
 #   if n>0:
#        break
#for i in range(n):
#        print("meow")


#function in Loops
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()