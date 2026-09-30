choice = int(input("Enter 1 for bike, 2 for car"))
if choice == 1:
    bike_type = int(input("Enter 1 for scooty, 2 for, motorbike:"))
    if bike_type == 1:
        print("You have picked scooty")
        print("Scooty - 80 km/hr") 
    else:
        print("You have picked motorbike")
        print("Motorbike - 120 km/hr")
elif choice == 2: 
    car_type = int(input("Enter 1 for Sports Car, 2 for Common Car:"))
    if car_type == 1:
        print("You have picked Sports Car")
        print("Koneisegg Jesko - 350 mph")
    else:
        print("You have picked Common Car")
        print("Honda Civic - 150 mph")