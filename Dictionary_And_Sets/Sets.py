# Set is data structure in python which stores Unordered, UNIQUE elements.
# Set is similar to set of dictionary keys and set values are hashed same as dictionary keys
# Elements in set must be IMMUTABLE objects just like dictionary keys however sets are MUTABLE
# It consists operations like union and intersection
# They are not used very often, however they are useful for clearing data
# We can define Sets just like dictionary

marvelCollections = {"Iron Man", "Iron Man 2", "Captain America - The First Avenger", "Iron Man 3", "Thor",
                     "Hulk", "Thor - The Dark World", "Avengers Assemble", "Captain America - The Winter Soldier"}
# marvelCollections.append("FUCk")       # Error : AttributeError
print(marvelCollections)        # We will observe that every time we run the order in not fixed
print("--"*60)

# Using set() contructor

marvelCollections = set(["Iron Man", "Iron Man 2", "Captain America - The First Avenger","Iron Man 3","Thor","Hulk",
                         "Thor - The Dark World", "Avengers Assemble","Captain America - The Winter Soldier"])

# it is not neccessary to create a set using constructors but however we need it for creating an empty set
# because if we use braces it will create empty dictionary

print(marvelCollections)
print("--"*60)
# We can pass any iterable object to create sets

num = set(range(0, 40, 2))        # NOTE : This set will not be in order
print(num)
num = set("12345667")
num_tuple = (2,3,3,5,3,7)
num = set(num_tuple)

print(num)      # We observed that duplication in omitted in the set
# O/P---> {'3', '1', '6', '4', '2', '5', '7'}
# num = set(2345678)                  # O/P---> TypeError: 'int' object is not iterable
# num = set("fuck")                     # O/P-->  {'f', 'c', 'k', 'u'}
# To add elements in set
marvelCollections.add("Ant Man")
marvelCollections.add("Ant Man")        # O/P remains same
marvelCollections.add(1)
# del marvelCollections[1]          # TypeError: 'set' object doesn't support item deletion
marvelCollections.remove(1)         # to remove elements

print(marvelCollections)
print("--"*70)

for number in num:
    print(number)           # But we cant say anything about its order

# Union Operation

evenNumbers = set(range(0, 50, 2))
square_numbers = {1, 4, 9, 16, 25}
unionSet = evenNumbers.union(square_numbers)
print("UNION OPERATION")

print(unionSet)
print("--"*50)

# Intersection Operation

print("INTERSECTION OPERATION")
intersection_set = evenNumbers.intersection(square_numbers)
print(intersection_set)
print("--"*50)

# Subtraction Operation

print("Subtract Operation")
subtracted_Set = square_numbers.difference(evenNumbers)
print(subtracted_Set)

# it can also be done as follows:

subtracted_Set = square_numbers - evenNumbers

print(subtracted_Set)
# using difference_update() method--> it updates the set with th resultant set, return type ---> None
square_numbers = {1, 4, 9, 16, 25}
square_numbers.difference_update(evenNumbers)
print(square_numbers)
# We can use following code too but using method is useful as it helps to recognise that variables are set object
# square_numbers = square_numbers - evenNumbers
# print(square_numbers)

evenNumbers = set(range(0, 50, 2))
square_numbers = {1, 4, 9, 16, 25}
# Symetric Difference Operator ----> it returns a set which is (union - intersection)
print(sorted(square_numbers.symmetric_difference(evenNumbers)))
# symmetric_difference() doest same work but it references to the same set who called it, retun type---> None

# IMPORTANT: They are two methods to delete elements from set:
# remove() ---> returns an error if elements not found
# discard() ---. returns no error if element not found

square_numbers.discard(67)
print(square_numbers)
# square_numbers.remove(67)             # O/P--> KeyError: 67
# print(square_numbers)
# we use remove if we had to handle the Error
try:
    square_numbers.remove(67)
except:
    print("ELEMENT NOT FOUND")

# SUBSETS - A set is Subset of B if all elements of A are present in B
# SUPERSET - B is SuperSet of A if it contains all the elements of A in it

evenNumbers = set(range(0, 50, 2))
square_numbers = {4, 16, 36}

if square_numbers.issubset(evenNumbers):
    print('Square Number is subset of Even Number')
if evenNumbers.issuperset(evenNumbers):
    print("Even number is super set of Square Number")

# Frozen Sets are sets which are Immutable and once created can not be changed
# it does not contains add(), discard(), and remove(), difference_update, intersection_update() methods
# it is useful for making keys for dictionary

even = frozenset(range(0,100,2))
# even.add(23)          # AttributeError
print(even)         # O/P--> frozenset({0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
#  42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98})
