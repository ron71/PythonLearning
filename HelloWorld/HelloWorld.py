print()
print("Hello")
print("""HEllo JOHN 
U ARE GREAT""")         #triple """ can be used its best to use

#important
print(""" "Hello" """)             #   we cant have 4 " in a row we must be saperated from triple quotes

print("'hsderisd HE'ssd'")

#   In python datatypes can be classified into numerics,sequences,mappings,files,classes, instances, exceptions.
#   In python 2 and below, it consist various datatypes like int, float, complex,long.
#   But python 3 doesn't supports long type and instead of it only int can be used.

#   note: Floating point nos takes more more time to compute than integer.

a = 13
b = 3                       #   OUTPUT:
print(a+b)                  #    15
print(a-b)                  #    9
print(a*b)                  #     36
print(a/b)                  #   4.0        --------------     '/' returns flaoting point value
print(a//b)                 #   4          --------------      '//' returns integer
print(a % b)                  #   0

#   now observe following:

#   for i in range(1,a/b):
#      print(i)                    #This will give Error as when we do a/b to returns floating value so incompatible datatypes

#   So following is right

for i in range(1,a//b):
        print(i)                                                    #output->  1,2,3

name = "ROHAN KUMAR";

print(name)                                                     #Output ->ROHAN KUMAR
print(name[3])                                                  #Output-> A  (important)
#print(name[15])                                   #     This will cause Error, Now no further written codes will be executed until the bug will be fixed
print("FUCK")

#       We can go for searching in reverse too

print(name[-3])                                               # O/P-> M                 NOTE : index like -0 is invalid
#       For printing substring from string                      print(String_name[range])

print(name[3:9])                        #       NOTE : Index 9 is excluded      O/P-> AN KUM
print(name[:9])                         # It will print from 0th index till 9th index i.e 8      O/P-> ROHAN KUM

print(name[3:])                         #It will  print till end        O/P ; AN KUMAR
print(name[-4:])                        #       O/P->   UMAR
print(name[:-3])                        #       O/P->   ROHAN KU
print(name[-1:3])                       #       Nothing will be printed
print(name[-2:-9])                      #       Nothing will be printed as substring specified must be in right side of starting index
print(name[-9:-2])                      #       O/P-> HAN KUM

# Characters can be skipped by counting steps after which the next character is to be taken

print(name[3:9:2])                      #   O/P->   A U             This will print every 2nd character starting from 3rd index till before 9th index

# This is helpul in many ways for example

number = "9,123,232,324,657,345,323"
print(number[1::4])                     # O/P->  ,,,,,,
number = "1,2,3,4,5,6,7,8,9"             #  O/P->   123456789
print(number[0::2])
print("Rohan" "Gonna" "Rock")           #   O/P->   RohanGonnaRock
print("Rohan" * 5)                      #   O/P->   RohanRohanRohanRohanRohan

#   We can search substring using 'in' operator

today = "Friday"

print("day" in today)                   #   O/P->   True
print("fri" in today)                   #   O/P->   False

print("fri" in "Monday")                   #   O/P->   False

test = "hello"" HE"
print(test)                             #   O/P-> hello HE

#       PRINTING STRINGS

print("CHECK THIS -> " + test + " iT worked")
year = 20#       O/P->   CHECK THIS -> hello HE iT worked
#   print("My age is "+year+"Years.")           #       ERROR: typecasting is required.
print("My age is "+str(year)+" years.")

# CONCEPT OF REPLACEMENT FIELDS

print("There are {0} sons of Pandav, they are {1}, {2}, {3}, {4}, {5}.".format(5,"Yudhistir","BHIM","ARJUN","NAKUL","SAHDEV"))

# using replacement fields made the working easy as we don't need to use typecasting and
# it is good for typing a long string in multiples lines.

print("""JANUARY : {2},
FEBRUARY : {0}, 
MARCH : {2}, 
APRIL : {1}""".format(28, 30, 31))


#       In Python 2 we can see written as
print("My age is %d years." % year)             # It will print same but here we use % for Replaacing the variable corresponding to appropriate type.
print("%s %d %s" % ("My age is", year, "years."))

for i in range(1,12):
        print("No. %2d squared is %4d and cubed is %4d"%(i,i**2,i**3))          #  here '%xd' creates apcing for atmost x no of digits

#       Remarks:        i ** x is equivalent to pow(i,x)

print("PI = %1.50f" % (22/7))                     # this is used for spacing in decimal places

# NOw we can do above formatting using replacement field method

for i in range(1,12):
        print("No. {:2} squared is {:4}d and cubed is {:4}".format(i, i**2, i**3))





