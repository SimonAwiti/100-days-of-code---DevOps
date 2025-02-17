name = input("what is your name? :")
currency = input(f"Hello {name} what currency do you want to convert your money into (ksh/usd)? :")
amount = float(input(f"How much do you want to convert into {currency}? :"))

if currency == "ksh":
    converted_currency = round(amount *129.15, 2)
    print(f"Dear {name}, your amount in {currency} is {converted_currency}")

elif currency == "usd":
    converted_currency = round(amount / 129.15, 2)
    print(f"Dear {name}, your amount in {currency} is {converted_currency}")
else:
    print(f"Dear {name}, your your currency is not accepted, kindly note that we accept usd/ksh")
    
