# start the quiz
print("Welcome to the True or False Quiz!")
print("Type 'true' or 'false'\n")

# question 1
print("Q1: The sun rises in the east.")
answer1 = input("your answer: ")
if answer1.lower()== "true":
    print("correct!\n")
    score1 = 1
else:
    print("wrong!\n")
    score1 = 0

# question 2
print("Q2: fish can walk on land")
answer2 = input("your answer: ")
if answer2.lower()== "true":
    print("wrong!\n")
    score2 = 0
else:
    print("correct!\n")
    score2 = 1
# final score
Total = score1 + score2
print("Your final score:", Total,"out of 2 ")
    
