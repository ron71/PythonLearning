import shelve

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

with shelve.open('map') as map:
    map['location'] = location
    map['directionsInWords'] = directionsInWords

