def distance_converter():
    km = float(input("Enter the distance in kilometers:"))
    miles = km * 0.6213
    print(km,"km =", miles, "miles")
def temperature_converter():
    celsius =float(input("Enter the temperature in celsius: "))
    fehrenheit = (celsius * 9/5)+32
    print(celsius, "°C=",fehrenheit,"°F")
while True:
    print("\n---unit calculator---")
    print("1. Distance (km to miles)")
    print("2. Temperature(celsius to fehrenheit)")
    print("3. Exit")

    choice = input("Choose an option (1-3):")

    if choice =="1":
       distance_converter()
    elif choice =="2":
       temperature_converter()
    elif choice =="3":
         print("Goodbye!")
         break
    else:
        print("Invalid choice. Please slect 1-3.")
