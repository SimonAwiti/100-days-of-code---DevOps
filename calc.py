#simple calculator that can add, subtract, multipy, or devide

operation = input("Enter an operation (+, -, *, or /): ")
number1 = int(input("Enter the first number :"))
number2 = int(input("Enter the second number :"))


if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
   print(number1 * number2)
elif operation == "/":
    print(number1 / number2)