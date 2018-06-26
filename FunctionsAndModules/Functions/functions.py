# Function are declared with "def" keyword.
# NOte: It is a convention to use 2 blank lines before and after declaration of function
# None return type and No arguments


def python_food():
    print("SPAM and EGGS")


# Calling:
python_food()

# return type and No argument


def python_drink():
    return 'Cola'


# Calling
print(python_drink())

# None return type and one or more arguments


def sum(a,b):
    print(str(a+b))
# Calling
sum(2,3)

# return type and one or more arguments


def sub(a, b):
    return a-b


# calling
print(sub(3,2))

# Concept of Call By value and Call by reference
list1 = list(range(0,51,2))


def list_modifier1(l):
    l.append('Fuck')
    print(l)


list_modifier1(list1)
print(list1)

# Above we can observe that both are giving same O/P, Therefore we conclude that list follows call by reference

# NOTE:


def list_modifier2(l):
    l=[3,4,5,4]
    print(l)


list_modifier2(list1)
print(list1)

# Concept of variable Arguments
print("*******************CONCEPTS OF VARIABLE ARGUMENTS**************************\n")
# variable arguments are written using "*"
# the variable returns a tuple
# NOte: and rest arguments are provided via their option names.


def variable_arguments(*args,b,c):
    for i in args:
        print(i)
    print(b,c)


variable_arguments(1,2,3,4,b=5,c=4)

print('***************************Making own print statement***************************************')


def centeredPrint(*args,sep=' ',end, file=None, flush =False):

    print(' '*40, end='')
    for i in args:
       print(str(i), sep=sep, end=end, file=file, flush=flush)


centeredPrint(1,'ada',23, end=':')

