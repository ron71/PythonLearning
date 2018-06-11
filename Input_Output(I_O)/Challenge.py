

import shelve
currentLocation = 1

with shelve.open('map') as map:
    while True:
        if currentLocation == 0:
            print('You are Dead\n')
            break

        else:
            availableLocation = ', '.join(map['location'][currentLocation]['directions'].keys())
            print('Current Location : {}'.format(map['location'][currentLocation]['desc']))
            print('Available destinations : {}'.format(availableLocation))
            usersInstruction = input("Where u wanna go?\n").upper()

            if len(usersInstruction) > 1:
                for word in map['directionsInWords']:
                    if word in usersInstruction:
                        usersInstruction = map['directionsInWords'][word]

            tempDictionary = map['location'][currentLocation]['directions'].copy()
            tempDictionary.update(map['location'][currentLocation]['place'])
            if usersInstruction in list(tempDictionary.keys()):
                currentLocation = tempDictionary[usersInstruction]



            else:
                print('No such routes available. Please try something else')


