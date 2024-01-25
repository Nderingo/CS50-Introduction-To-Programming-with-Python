import re

email = input("What is your email address? ").strip()

#username, domain = email.split("@")

#if username and domain.endswith(".edu"):
#    print("Valid")
#else:
#    print("Invalid")

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")