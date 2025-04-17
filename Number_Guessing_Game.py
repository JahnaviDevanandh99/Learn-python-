#Number Guessing Game
print("Welcome to the Number Guess Game!")
import random
secret_number = random.randint(1, 50)
guess=29
Name=input("Enter Your Name:")
print("Guess the secret number between 1 and 50!")
while guess !=secret_number:
    guess = int(input("your guess:"))
    if guess < secret_number:
        print("too low, try again!")
    elif guess > secret_number:
        print("too high, try again!")
    else:
        print("you got it",Name,"!",",Well done!")
