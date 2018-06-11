for i in range(1, 21):
        print("This is no {: 2}.".format(i))

data = "123,1232,24h234gg21ui3h123,1j3h1283123j78e2e3m3bsi3ubi455wyf89w96671321830313,12092769122p0913./';[3123612312"

print(len(data))
for i in range(0, len(data)):
        print(data[i])

#     Suppose you are given a huge data and
#      we have to use essential elements of it so have to slice the data to fetch the essentials.
print("\n************************************************************\n")
st = ""
for i in range(0, len(data)):
        if data[i] in "1234567890":
            st += data[i]
print(st)

for i in range(0, len(st)):
        if st[i] in "12345":
            print(st[i], end='')           # here we override the print() command by default it is print(data,end="\n')

# Another version
print("\n************************************************************\n")
for char in data:
        print(char)

print("\n************************************************************\n")

for state in ["Bihar", "Jharkhand", "Orissa"]:
    print(state)

#     range(starting index, closing index) ----> this auto increments the index by one till closing index
#     however we can override the incrementation i.e

print("\n************************************************************\n")

for i in range(0, 100, 5):                  # here we are auto incrementing by 5 i.e i=i+5;
        print(i)

print("\n************************************************************\n")

for i in range(1, 16):
    print("Table of {}\n".format(i))
    for j in range(1, 11):
        print("{0}\tX\t{1}\t=\t{2}".format(i, j, i*j))
    print("\n************************************************************\n")

print("\n************************************************************\n")

#   For loop with else statement

bad_food = ""
meal = ["eggs", "spam", "becon", "milk"]
for i in meal:
    if i == "spam":
        bad_food = i
        break
else:               #   THIS WILL BE CALLED IF BREAK STATEMENT NOT CALLED
    print("This is else part\n")

if bad_food:
    print("BAD_FOOD\n")

#   Example No-2

for i in range(0, 101):
    if i % 2 == 0:
        print("EVEN\t"+str(i))
else:
    print("ODD\n")      # this can only be added when for loop contains if statement and it always executes after complete execution for loop


#   Another variation

for i in range(0, 101):
    if i % 2 == 0:
        if i % 4 == 0:
            print("EVEN by 4\t"+str(i))
else:
    print("ODD\n")

print("\n************************************************************\n")

#   Important:-

ip_address = "192.168.43.204"
for char in ip_address:
    if char == ".":
        print("THERE IS A DOT");
    else:
        print(char, end="")

if char != ".":
    print("\n"+str(char))

#   Note: In java, C++ the local variable of for loop is not accessible outside the loop,  But its different for python.
#   it can accesses if THE FOR LOOP EXECUTES AT LEAST ONCE, i.e one true case.
del char        #   Here we unreferenced the char variable
print(char)     #   now it will cause error
