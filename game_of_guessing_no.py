#A game of number guessing

right_no = 25

guess = int(input("Guess any number between of your choice :"))

while guess != right_no:
    if guess > 30 or guess < 10:
        print(f"{guess} is out of range, Hint (between 10 - 30)")
        guess = int(input("Guess again! :"))
    else:
        guess = int(input("You are close...Guess again! :"))

print("Hooray! You are our lucky winner")
        
                  

