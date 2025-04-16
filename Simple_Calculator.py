# simple calculator
print(" Welcome to the Simple Calculator ")

# add the functions 
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "error!, Division by zero."
    return x/y

# main program
print("Select the operation")
print(" 1. Add")
print(" 2. Subtract")
print(" 3. Multiply")
print(" 4. Divide")

choice = input("Enter choice (1/2/3/4):")
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number :"))

# result for the each choice of the user
if choice == '1':
    print("The Result is :", {add(num1,num2)})
elif choice == '2':
    print("The Result is :", {subtract(num1,num2)})
elif choice == '3':
    print("The Result is :", {multiply(num1,num2)})
elif choice == '4':
    print("The Result is :", {divide(num1,num2)})
else: print("Invalid input")    
