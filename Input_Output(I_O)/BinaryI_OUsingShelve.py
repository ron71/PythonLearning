# Drawback of pickle is that, whenever we wanted any data we have to restore entire file in memory
# via making their objects. So it is not good of very large files.
# Therefore python has one more module called shelve,
# this module is too recommended to not to be used with untrusted file sources like internet
# It stores value in key object pairs just like dictionaries,
# it stores using key value and values are pickled and then stored
# IMPORTANT :  SHELVE KEYS MUST BE STRINGS while dictionary can have any immutable object

import shelve

with shelve.open('shelveTest') as fruit:
    fruit['apple'] = 'An apple a day, keeps doctors away'
    fruit['grape'] = 'Larely used for making resins and alcohol'
    fruit['mango'] = 'They are king of fruit in Summer'
    fruit['watermelon'] = 'Greater in size more juice they have'
    fruit['orange'] = 'A citrus sweet source of vitamin C'

    print(fruit['apple'])
    print('*'*80)

    for key in fruit:
        print(key)

# print(fruit['apple'])         # O/P--> ValueError: invalid operation on closed shelf
# AS shelve is closed we cannot access file

# in dictionary we can create it using literals but shelve cannot be created by using literals
# Note : Shelve files are persistent i.e. if we created a shelve file which contains a key value,
# Howewer on second run we changes the value the value of key and run the file
# We will observe that the old key value pairs are still there
# that means when we ran the file second time it didn't erased the last entries rather it appended few more
# Just like dictionary they are unordered
# It too creates KeyError if we try to access key which is not present so it would be better using get() method
# It returns None if key not found
    print('*'*80)
    while True:
        dict_key = input('Enter The key')
        if dict_key == 'quit':
            break
        print(fruit.get(dict_key, 'We don\'t have '+ dict_key ))

print('line - 41\t'*20)
fruit =  shelve.open('shelveTest')
for key in fruit:
    print('{0} - {1}'.format(key,fruit[key]))

print()
print("line - 47\t"*10)
print(fruit.keys())     # NOTE : Instead of dict_keys object it returns KeysView
print(fruit.items())    # NOTE : Instead of dict_items view it returns ItemsView
print(fruit.values())   # NOTE : Instead of dict_values object it returns ValuesView
# All three are view object i.e. we cant modify them
fruit.close()       # This line is must if we open a without 'with'


# Updating data in shelves

with shelve.open('shelveTest') as recipe:
    recipe['maaggi'] = ['water', 'Boiler', 'Maggi']

# now we try to update data
with shelve.open('shelveTest') as recipe:
    recipe['maaggi'].append('veggies')

with shelve.open('shelveTest') as recipe:
    print('Recipe for maggi : {}'. format(recipe['maaggi']))
    # O/P--> Recipe for maggi : ['water', 'Boiler', 'Maggi']
# we can see the list didn't modified this is because
# although we appended the list it was not triggered by shelve to save the modification in the file.
# We just appended to a copy of list wich was loaded in the memory from file

# So there are two ways to modify the content:

# First way is to copy the list in a temporary list and then append the data in the temp. list
# and finally copying the temp. list back to the shelve

print()
print('    Line No - 77\t********'*50)
with shelve.open('shelveTest') as recipe:
    tempList = recipe['maaggi']
    tempList.append('veggies')
    recipe['maaggi'] = tempList

with shelve.open('shelveTest') as recipe:
    print('Recipe for maggi : {}'. format(recipe['maaggi']))


# Another way is to open the shelve file in 'writeback' mode = True and then append the content

with shelve.open('shelveTest', writeback= True) as recipe:
    recipe['maaggi'].append("Taste Maker")

with shelve.open('shelveTest') as recipe:
    print('Recipe for maggi : {}'. format(recipe['maaggi']))
# Python caches the data in memory and updates the data in the shelve at the time of closing the file
# Actually a 'sync' method is called at the time of closing the file, so it loads the data in the disk
# and clears the cache (Important)
# So it can take a while to close the file if there are so many modification in the file
# This is because all modification are to be written in disk/file
# This becomes an disadvantage in case of huge amount of data

# Using sync() method:
# Note : It works under write back mode = True

with shelve.open('shelveTest', writeback= True) as recipe:
    recipe['maaggi'].append('2 minutes')
    recipe.sync()
print()
print('    Line No - 108\t********'*50)
with shelve.open('shelveTest') as recipe:
    print('Recipe for maggi : {}'. format(recipe['maaggi']))

