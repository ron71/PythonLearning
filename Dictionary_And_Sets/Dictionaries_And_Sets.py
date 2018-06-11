# While list is ordered sequence type, dictionaries are Unordered sequence type
# In dictionaries items stored in key value pairs, which cannot be accessed through index but by means of key
# Lists are generally used to keep similar items but dictionaries can keep heterognous items.

avengers = {"Captain America": "The first Avenger - Capt. Steve Rogers",
            "Iron Man": "PlayBoy - Tony Stark",
            "Black Widow": "A Soviet assassin working for shield - Natasha Romanoff ",
            "Hawk Eye": "A archer - Clint Barton",
            "Hulk": "A Biological Scientist - Bruce Banner",
            "Thor": "Son of Odin, King of Asgard"}
print(avengers)

# Instead of index we will use key to access
print(avengers["Black Widow"])          # O/P---> A Soviet assassin working for shield - Natasha Romanoff
# If key not found causes Error : KeyError

avengers["Black Widow"] = "Agent for Shield, formaly Assassin for Soviet union"
print(avengers["Black Widow"])          # O/P---> Agent for Shield, formaly Assassin for Soviet union
# We can see dictionaries are mutable i.e Value of elements can be changed

# Inserting new item in dictionary :
avengers['Scarlett Witch'] = "A Experiment done by hydra"

print(avengers)

# Important : Key must be unique in dictionary
# to clear the dictionary clear() function is used
#
# avengers.clear()
# print(avengers)
# print(avengers["Captain America"])
# while True:
#     dict_key = input("ENTER AGENT NAME")
#     if dict_key == "quit":
#         break
#     description = avengers.get(dict_key, "Agent not found")
#     print(description)

# It recommended to use get() method as it returns None if key not found instead of Error if we do not provide any other
# message or prompts
# We can use in keyword to check for availability of an key

print("Hulk" in avengers)
# In python 2 same work was done by _has_key() method it is deprecated from Python 3

# Example :
for i in range(10):
    for agentKey in avengers:
        print("{0:15} : {1}".format(agentKey, avengers[agentKey]))
    print("-" * 60)

# Dictionary has unordered data that means whenever we add or delete a key the order could change
# So whenever we have to iterate through the dictionary we should make it ordered

print("--"*50)

for agentKey in sorted(avengers.keys()):
    print("{0:15} : {1}".format(agentKey, avengers[agentKey]))
print("*" * 60)

# Or simply this can do the work
print(sorted(avengers.values()))         # this will print a list of sorted values only not keys
# NOTE : There is a ordered dictionary in collection library (To be seen later)
print(avengers)         # it again becomes unsorted
print(avengers.keys())      # it returns dict_keys object
print(avengers.values())    # it returns dict_values object
# And both are known as View objects

# Important:
dict_view = avengers.keys()

avengers["Vision"] = "The Mind Stone keeper"
# Now dict_view is automatically updated
print(dict_view)
# Another type of a View is dict_items

print(avengers.items())         # it returns a dict_items view inform of list containing tuples in key value pairs

print(tuple(avengers.items()))

# Creating a dictionary from tuple using dict() constructor

trophyTuples = ((2008, "RR"), (2009, "DC"), (2010, "CSK"))

trophyDictionary = dict(trophyTuples)
print(trophyDictionary)

# COPYING TO Dictionaries

guardiansOfGalaxy = {"StarLord": "Funny but caring being",
                     "Gamora": "Green killer and so called daughter of Thanos",
                     "Groot": "a cute but dangerous plant alien",
                     "Rocket": "A veteran rokoon",
                     "Drax": "A angry beast",
                     "Nebula": "Poisonous daughter of Ronin"}

# Use of update() method

# avengers.update(guardiansOfGalaxy)      # This line copies whole dictionary to avengers
infinityWar =  avengers.copy()                      # copy returns dictionary object
infinityWar.update(guardiansOfGalaxy)               # update returns 'None'

for agentKey in infinityWar.keys():
    print("{0:15} : {1}".format(agentKey, infinityWar[agentKey]))
print("-" * 60)
