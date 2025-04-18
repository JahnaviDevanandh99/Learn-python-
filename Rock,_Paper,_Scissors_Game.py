import random

print("Welcome to Rock, Paper, scissors!")
print("Type 'quit' to stop playing.\n")

while True:
    #to get player's choice
    Player= input("Choose Rock, Paper, or Scissor: ").lower()

    if Player == "quit":
        print("Thanks for playing!")
        Break

    # Get computer's choice randomly
    computer= random.choice(["rock","paper","scissors"])

    print("You chose:", Player)
    print("Computer chose:", computer)

    # to decide winner
    if Player == computer:
           print("It's a tie,Buddy!\n")
    elif(
        (Player == "rock" and computer == "scissor")or
        (Player == "scissor" and computer == "paper")or
        (Player == "paper" and computer == "rock")
         ):
            print("You win,Buddy!\n")
    else:
        print(" oops,Computer wins!" + " better luck next time !")
     
