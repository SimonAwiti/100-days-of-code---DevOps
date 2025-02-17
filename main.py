#While loops: executes code provided that the condition remains true

name = input("Enter your name :")

while name == "":
    print ("You did not enter your name")
    name = input("Enter your name :")

print(f"Hello {name}!")
    
