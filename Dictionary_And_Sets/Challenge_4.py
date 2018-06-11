# Here we extended Challenge 3 and now permitting user to type place name too:
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
                     "QUIT": "Q",
                     "BUS STOP": "1",
                     "SHIKHARCHANDI": "2",
                     "HOSTEL": "3",
                     "CAMPUS-6": "4",
                     "KIIMS": "5"}

paths = {1: {"2": 2,"3": 3,"5": 5, "4": 4},
         2: {"5":5},
         3: {"1":1},
         4: {"1": 1, "2": 2},
         5: {"1": 1, "2":2}}
# routes = pathToHome.copy()
# routes.update(paths)
# for key in routes:
#     print('{0} : {1}'.format(key,routes[key]))
# Above we observe that keys are overridden

currentLocation = 1
while True:
    availAbleLocation = ",".join(pathToHome[currentLocation].keys())

    if currentLocation == 0:
        print("You are Dead NOW")
        break
    else:           # we will combine paths and path to home dictionary together
        routes = pathToHome[currentLocation].copy()
        routes.update(paths[currentLocation])
        # for key in routes:
        #     print('{0} : {1}'.format(key,routes[key]))

    directionProvided = input(" AVAILABLE DIRECTIONS : " + availAbleLocation + "\t").upper()
    if len(directionProvided) > 1:
        for word in directionsInWords:
            if word in directionProvided:
                directionProvided = directionsInWords[word]
                break



    if directionProvided in routes:
        currentLocation = routes[directionProvided]
        print("CURRENT LOCATION : " + location[currentLocation])
    else:
        print("ENTER VALID DIRECTION")

