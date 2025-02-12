#vTypecasting: converting to str() float() int() bool()

age = 29
name = "Simon Awiti"
is_student = False 
gpa = 4.5

if is_student:
    print (f"my name is {name} and I'm {age} years old and Im a student")
else:
    print (f"my name is {name} and I'm {age} years old and Im Not a student")
    
    
print (type(age))

gpa = int(gpa)

print (gpa)

#typecasting a string into a bool 

name = bool(name)

print (name)