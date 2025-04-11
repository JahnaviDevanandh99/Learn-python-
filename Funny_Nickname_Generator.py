print("Welcome to the funny Nickname Generator")
name=input("Enter your name :")
print(" Choose a title for your name ")
print(" 1. The Brave ")
print(" 2. The python pro ")
print(" 3. The silent ninja ")
print(" 4. The sunshine ")
choice = input("Enter 1,2,3 or 4 ")
if choice == "1":
   title = " The Bravo "
elif choice == "2":
     title = " The python pro "
elif choice == "3":
     title = " The silent ninja "
elif choice =="4":
     title = " The sunshine "
else:
    title=" The mystery one "

nickname = name + " " + title
print(" your nickname is :",nickname)
print(" Nickname length is :",len(nickname))
