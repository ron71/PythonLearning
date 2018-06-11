#   Python consists 7 types of sequence types they are:
# String
# List
# Tuple
# Range
# And three binary sequences (to be discussed later)
# These above are ordered sequence types i.e. they can be accessed through their index no.

# list : List is a sequence type that can store string, nos, classes etc.

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
number = even + odd
print(number)

number.sort()
print(number)

# imp: sort() method returns 'None'
print(number.sort())

#   sorted(list)--> this function return a sorted list of same type elements

num = [322, 454, 324, 575, 334, 8, 57, 34478, 10]
print(sorted(num))
print(num)          # however num is not sorted
num.sort()
print(num)

num1 = [322, 454, 324, 575, 334, [84, 57, 34478], 10]
# print(sorted(num1))         # error
print(num1[2:6])         # 6th index is not included till 5th index will printed

print(num1[::3])         # Traverses whole list (including heterogeneous list) with step size of 3

print(num1.index(454))   # returns index of first occurence of the element

#   append method:

num1.append("Fuck")
print(num1)
num1 = num1+["FUCK AGAIN"]
print(num1)

#   insert method : Similar to append with additional feature of inserting at specified index
num1.insert(5, 'fuck me at last')
print(num1)

#   List constructor

list1 = []
list2 = list()
print("List1  : {}".format(list1))
print("List2 : {}".format(list2))
#   both are same and in 2nd one we have used list contructor
if list1 == list2:
    print("EQUAL")

#   Parametrised constructors
list3 = list("Scarlett Johnson")
print(list3)
# print(list(34234, 23423, 342, "sudfiouo"))     # Error -->   List() takes only one argument

# Note: All sequence type are Iterable

even = [2, 4, 6, 8]
anotherEven = even
#   Note : both are pointing to same list object
print(anotherEven is even)      # O/P--> True
anotherEven.sort(reverse=True)      # In descending order
print(even)                     # O/P-->    [8, 6, 4, 2]

#   BUT when we use a list constructor always a new object is formed
anotherEven = list(even)
print(anotherEven is even)      # O/P-->    False

print(anotherEven == even)      # This campares the contents of the list

# but in java '==' checks reference just like 'is' in python

# RANGES

# In Python 2 range was a function while in Puthon 3 range is a built in function
# Any type of range takes same space in memory
r1 = range(1000)
r2 = range(100)
print(r1)       # O/P--> range(0,100)

# both r1 and r2 have same space in memory
# however if we create list with these ranges this will take memory as per range because lists need to expand
print(list(r2))

r3 = r1[5:97:5]
print(r3)           # O/P--> range(5,97,5)

r3 = r1[::5]
print(r3)           # O/P--> range(0,1000,5)

print(r3 == range(0, 1000,5))   # O/P-->    True

print(range(0, 5, 2) == range(0, 6, 2))     # O/P--> True
# IMPORTANT : Ranges are not checked on their limits and step step size
# rather they are checked on the basis of their actual content of nos.

print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

# We observe that both list are same there both ranges are equal
r = range(0, 100)

for i in r[::-2]:
    print(i)

print("*"*150)

for i in range(99, 0, -2):
    print(i)
# Both the codes are same both same output

print(list(range(99, 0, 2)))          # O/P--> []       This is not of sense

# Ranges can start from bigger no to smaller no iff step size is negative

print("*"*80)
for i in range(99, -1, -1):             # O/P---> numbers from 99 to 0
    print(i)

s = str(num)    # O/P--> [8, 10, 57, 322, 324, 334, 454, 575, 34478]
print(s)

# join() method is just opposite of split()
alpha = ["a", 'b', 'c']
s = "-->".join(alpha)
print(s)            # Now s is a string O/P-->  a-->b-->c

# s = "-->".join(num)           # Error as num stores int values
