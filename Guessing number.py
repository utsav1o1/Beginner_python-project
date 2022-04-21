import random

numberofguesses = 0

print("Hello! what is your name ?")
name = input(print("Hello! what is your name ?"))

number = random.randint(1,20)

print(" 1. You can guess only one time. Mrs/Ms", name)
print("2. You can guess number between 1 to 20. Mrs/Ms", name)

while numberofguesses < 6 :
    guess = input("Guess the number ")
    guess = int(guess)
    numberofguesses= numberofguesses+1;
    guessesleft = 6-numberofguesses;

    if guess < number :
        guessesleft=str(guessesleft)
        print("Your guess is too low! You have " + guessesleft + " guesses left")
    if guess > number :
        guessesleft = str(guessesleft)
        print("Your guess is to high! You have" +  guessesleft + "guesses left" )
    if guess == number :
        break
if guess == number:
    numberofguesses = str(numberofguesses)
    print("Good job! You guessed the number in " + numberofguesses + " tries :)")

if guess != number:
    number = str(number)
    print("Sorry. The number I was thinking of was " + number + " :)")
