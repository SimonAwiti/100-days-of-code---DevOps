#Password validator (should have 8 characters or more, no space, no digits)

password = input("What is your password? :")



if len(password) <= 8:
    print("Your password must contain more than 8 characters")
elif not password.find(" ") == -1:
    print("Your password must contain no spaces")
elif not password.isalpha():
    print("Your password must contain alphabets")
    
else:
    print(f"Welcome, your password is {password}")
