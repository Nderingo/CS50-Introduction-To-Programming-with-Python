print('Hello World!')
print('Create Hummer!')
print('Create Nails')
print('Use Hummer and Nails to create')

# Variables
failed_subjects = " 6"
name="John"
print('Dear Mrs Lyimo')
print(name + ' is failing' + failed_subjects + ' subjects')
print( name + ' will have to redo' + failed_subjects + ' subjects')
name="Richard"
print('But ' + name + ' is good in Math')

# Naming of variables in python should be in one word using underscore or using camel cases
# strings = are asigned with either "" or ''
print(type('hello'))

# Data types

# Integers = They are whole numbers 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
print(type(1))

# TypeCasting
a = int(2)
b = float("6")
b2 = float("4.989786")
c = float('3.786')
d = int(float("3.4"))

print([a,b,b2,c,d])
# Floats = These are decimal numbers 1.2, 3.6 etc
print(type(1.64))
# Boolean = These are data that can take the value of true or false
print(type(True))

# Data Types and Variables Exercise

freshVegetables = "asparagus"
price = 2.99
in_stock = True
stock = 100
print([freshVegetables,price,in_stock,stock])

# Arithmetic operations
a = 8
b = 3
print('Add :', a+b)
print('Sub',a-b)
print('Multiplication',a*b)
print('Div (float)',a/b)
print('Modulus',a%b)
print('Division',a//b)
print('Exp',a**b)

# Strings-Basics Slicing
message = 'Welcome to Python 101 strings!'
print(message,message)
print(message + message)
print(message*5)
print(message.upper()*2)
print(message.lower())
print(message.capitalize())
print(message.title())
print(len(message))
print(message.count('e'))

# Slicing Strings Getting part of the string s and returninfg them

print(message[2])
print(message[:8])
print(message[-8])

# String Exercise
msg = "Welcome to Python 101:Strings"
msg1 = msg[18] + " " + msg[:8] + msg[24:28]+msg[7:11] +msg[8]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1].title())

# Finding and replacing in Stringd
msg = "Welcome to Python 101:Strings"
print(msg.find('h'))
print(msg.replace('Welcome to','Karibu kwenye'))

# membership
print('Python' in msg)
print('Python' not in msg)

# string formating







