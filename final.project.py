# function to prompt user and return value entered
def promptUserForInput(prompt):
    response = int(input(prompt))
    return response


#start car buying menu
print ("Welcome to Joe's Car Shack")

purchaseVehicle = "y"

while (purchaseVehicle == "y"):
    vehicleType = promptUserForInput("Do you want to buy a car [1] or truck[2]?")
    if vehicleType == 1:
        basePrice = 1000
    elif vehicleType ==2:
        basePrice = 2000
    else:
        print("Please enter a 1 or 2")
        exit()

    engineType = promptUserForInput("Do you want a V6 [1] or a V8 [2]?")
    if engineType == 1:
        engineCost = 300
    elif engineType == 2:
        engineCost = 500
    else:
        print("Please enter a 1 or 2")
        exit()

    color = int(input("Do you want blue [1] or red [2]?"))
    if color == 1:
        colorCost = 100
    elif color == 2:
        colorCost = 200
    else:
        print("Please enter a 1 or 2")
        # TODO this crashes
        exit()



    total = basePrice + engineCost + colorCost
    print ("The total cost of your vehicle is: " +str(total))

    purchaseVehicle = input("Do you want to purchase another vehicle? y/n").lower()
