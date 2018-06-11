# We no need to import the modules from standard library
# as these core built in modules are automatically imported in the program
# using dir() method : We can use to see what are the methods or modules imported automatically or imported explicitly
import random
print(dir())
# O/P--> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#          '__package__', '__spec__']
# Important : anything whose name start with double underscore '__' , is recommended not to be changed or modified.
# There is no concept of private variables in python but for convention
# anything which is need to not to be altered should start with double underscore and is to be private to the module

# if we see the O/P of dir() function, not all the modules are for programming point of view,
# some are for internal working of Python
# '__builtins__' it contains all the built in literals and functions
# So we can see all the funtions through documentation or by folowing code;
print(dir(__builtins__))
count = 0
for literals in dir(__builtins__):
    count+=1
    print('{0:3} - {1}'.format(count,literals))

help(random)    # it provides whole prototype description of module
help(random.randint)