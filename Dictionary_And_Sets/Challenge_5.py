# This challenge extends Challenge 4 as now all the dictionary are in one

location = {0: {"desc": "Dead",
                "directions":{"Q": 0},
                "place": {}},
            1: {"desc": "At Bus Stop",
                "directions":{"W": 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},
                "place": {"2": 2,"3": 3,"5": 5, "4": 4}},
            2: {"desc": "At Top of Shikharchandi",
                "directions":{'N': 5, 'Q': 0},
                "place": {"5":5}},
            3: {"desc": "At Hostel",
                "directions":{'W': 1, 'Q': 0},
                "place": {"1":1}},
            4: {"desc": "At Campus-6",
                "directions":{'N': 1, 'W': 2},
                "place": {"1": 1, "2": 2}},
            5: {"desc": "At KIIMS",
                "directions":{'S': 1, 'W': 2},
                "place": {"1": 1, "2":2}}}

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

currentLocation = 1

while True:
    availableLocation = ",".join(location[currentLocation]["directions"])

    if currentLocation == 0:
        print("YOUR ARE DEAD NOW")
        break
    else:
        routes = location[currentLocation]["directions"].copy()
        routes.update(location[currentLocation]["place"])

    directionsinstruction = input("ENTER THE DIRECTION OR PLACE : {}\t".format(availableLocation)).upper()

    if len(directionsinstruction) > 1:
        for word in directionsInWords:
            if word in directionsinstruction:
                directionsinstruction = directionsInWords[word]
                break

    if directionsinstruction in routes:
        currentLocation = routes[directionsinstruction]
        print("Current Location : {}".format(location[currentLocation]["desc"]))
    else:
        print("ENTER VALID INSTRUCTION")
        print("Current Location : {}".format(location[currentLocation]["desc"]))

