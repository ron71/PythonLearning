# It is extension of Challenge-2, Now user will provide direction in words
# User can also type instruction like go North, going north, I want to go no north etc

location = {0: "DEAD",
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

directionsInWords = {"NORTH": "N",
                    "SOUTH": "S",
                    "WEST": "W",
                    "EAST": "E",
                    "QUIT": "Q"}

currentLocation = 1
while True:
    availAbleLocation = ",".join(pathToHome[currentLocation].keys())

    if currentLocation == 0:
        print("You are Dead NOW")
        break

    directionProvided = input(" AVAILABLE DIRECTIONS : " + availAbleLocation + "\t").upper()
    if len(directionProvided)>1:
        for word in directionsInWords:
            if word in directionProvided:
                directionProvided = word
                break

    if directionsInWords[directionProvided] in availAbleLocation:
        currentLocation = pathToHome[currentLocation][directionsInWords[directionProvided]]
        print("CURRENT LOCATION : " + location[currentLocation])
    else:
        print("ENTER VALID DIRECTION")

