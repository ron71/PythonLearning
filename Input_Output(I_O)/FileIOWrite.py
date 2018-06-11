# we will use open method with write operation 'w'
# We will print the elements inside the file using print function and we aill provide file object in the print function
# We must close the file to fluch the buffer, so its better to open the file using 'with' keyword

cities = ['Bokaro', 'Ranchi', 'Hazaribaagh', 'Deoghar', 'Simdega', 'DaltonGunj']
with open('Sample_Cities.txt','w') as citiesFile:
    print(cities, file=citiesFile)      # Printing whole cities at once will store in form of list as string
    for city in cities:
        for letter in city:
            print(letter, file=citiesFile,end='--')
        print(city, file=citiesFile)

    imelda = "More Mayhem", "Imelda May", 2011, (
        (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"Kentish Town Waltz"))
    print(imelda, file=citiesFile)  # Whole tuple will be inserted in form of String

    album, artist, year, track = imelda
    print(artist,file=citiesFile)
    print(album, file=citiesFile)
    print(year, file=citiesFile)
# We can not show what written in file in original form
with open('Sample_Cities.txt','r') as citiesFile:
    for line in citiesFile:
        print(line, end='')

print("0"*100)
# we can takeout values in form of their object like tuple, list, dictionary etc using eval() method


with open('Sample_cities.txt', 'w') as citiesFile:
    imelda = "More Mayhem", "Imelda May", 2011, (
        (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"Kentish Town Waltz"))
    print(imelda, file=citiesFile)

with open('Sample_cities.txt', 'r') as citiesFile:
    line = citiesFile.readline()
    imelda = eval(line)
    print(imelda)
    album, artist, year, track = imelda
    print(album)
    print(artist)
    print(year)
    print(track)

# Appending in file is shown in Challenge_1
