# In this challenge we will be converting oathto home in dictionary
# containing numbers as key and the available routes as value

location = {0: "Home",
            1: "At bus stop",
            2: "At Top of Shikharchandi",
            3: "At Hostel",
            4: "At Campus 6 Audi",
            5: 'At KIIMS'}

pathToHome = {0: {"Q": 0},
              1: {"W": 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},
              2: {'N': 5, 'Q': 0},
              3: {'W': 1, 'Q': 0},
              4: {'N': 1, 'W': 2},
              5: {'S': 1, 'W': 2}}

currentLocation = 1
while True:
    availAbleLocation = ",".join(pathToHome[currentLocation].keys())

    if currentLocation == 0:
        print("You are HOME NOW")
        break

    directionProvided = input(" AVAILABLE DIRECTIONS : " + availAbleLocation + "\t").upper()
    if directionProvided in availAbleLocation:
        currentLocation = pathToHome[currentLocation][directionProvided]
        print("CURRENT LOCATION : " + location[currentLocation])
    else:
        print("ENTER VALID DIRECTION")