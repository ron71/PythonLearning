# Tuples are ordered sequence type same as Lists, Only difference is that Tuples are immutable
#  i.e. we cant change its contents.
# However we can assign the variable with new tuple
# It is recommended to keep tuples in parenthesis which is optional this help in resolving the ambiguity.

drinks = "Coca_cola", "Thumbs_Up", "RedBull", "Tuborg", 1998, False
food = ("Eggs", "Beacon", "Spam", "Milk")
print(("kiss", "fuck", "enjoy"))    # We can see parenthesis differentiates tuple from print statement

# Above All are examples of tuples
# Accessing elements
print(food[3:0:-2])        # Same as List

# Checking Immutability
# food[1] = "Chicken"     # ERROR - TypeError: 'tuple' object does not support item assignment
# however we can reassign whole tuple
food = food[0], "Chicken", food[2], food[3]
print(food)

# Important: Tuples are preferred to store Heterogenous items
# List are preferred to store Homogenous items

# We always use tuples were we don,t want the data to be changed during runtime.

# UNPACKING OF TUPLES ----------------:

# we can multiple variables with same value at a time
a = b = c = 12
print(b)

# We can also assign multiple var with multiple values at a time

a, b = 12, 13
print("A is {0} and B is {1}".format(a, b))

a, b = b, a
print("A is {0} and B is {1}".format(a, b))
# NOTE : First of right side side elements of  assignment operator is handelled than left side

# If we see in line 32, it is more like tuple,
# We can assign variables through tuple and we must assign variables to all elements of tuple

yeWatan = ("Ye Watan Watan", "Arijit Singh", 2018)

album, artist, year = yeWatan
print('ALBUM : {0}\nARTIST : {1}\nYEAR : {2}\n'.format(album, artist, year))


listSong = list(yeWatan)
print(listSong)

# Tuples do not have append() function

# Challenge :

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"Kentish Town Waltz"))

print(imelda)

album, artist, year, tracks = imelda

print('ALBUM : {0}\nARTIST : {1}\nYEAR : {2}\n'.format(album, artist, year))

for i in tracks:
    trackNo, trackName = i
    print("{} - {}".format(trackNo, trackName))

# Now suppose there is a list inside the tuple, so However tuple is immutable items of list can be changed

imelda = "More Mayhem", "Imelda May", 2011, [
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"Kentish Town Waltz")]

album, artist, year, tracks = imelda
tracks[3] = (4, "Lipstick")

print(imelda)
