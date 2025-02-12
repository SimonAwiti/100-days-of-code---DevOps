#input 
name = input("What is your name? : ")
age = int(input(f"Hi {name}, how old are you? : ")) #typecast the input into an int 

age = age + 1

print(f"Hello {name}, HAPPY BIRTHDAY! You are {age} years old")