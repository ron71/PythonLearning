location = {0: "Home",
            1: "At bus stop",
            2: "At Top of Shikharchandi",
            3: "At Hostel",
            4: "At Campus 6 Audi",
            5: 'At KIIMS'}

pathToHome = [{"Q": 0},
              {"W": 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},
              {'N': 5, 'Q': 0},
              {'W': 1, 'Q': 0},
              {'N': 1, 'W': 2},
              {'S': 1, 'W': 2}]

currentLocation = 1
while True:
    availableRoutes = ",".join(pathToHome[currentLocation].keys())
    directionProvided = input("Available directions to go " + availableRoutes + "\t").upper()
    if currentLocation == 0:
        print("\nYour are HOME NOW ")
        break
    if directionProvided in availableRoutes:
        currentLocation = pathToHome[currentLocation][directionProvided]
        print("\nCurrent Location : "+location[currentLocation])
    else:
        print("Not a Valid Direction")


