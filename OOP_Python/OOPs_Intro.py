class Kettle(object):
    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


""" Constructor is method which is called when instance of the class is created.In python constructors are made in two steps.
first, be using new as a method __new__() to create instance, then __init__ to initialize the data members if any.
However its not necessary to write the new method as is it invoked automatically."""

kenwood = Kettle("Kenwood", 20.9)
hamilton = Kettle("HAMILTON", 67.3)

print("{}={}\t{}={}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print(hamilton)
print(kenwood)
print("{0.make}={0.price}\t{1.make}={1.price}".format(kenwood, hamilton))
# In case ob accessing data attribute of any object we can use the above method
#     too in the replacement fields

# we can see that every method inside a class has 'self' keyword, This self is a reference to the instance of the class.
# We can also write in following way by providing instance in position of self.
Kettle.switch_on(kenwood)
print("SWITCH ON : {}".format(kenwood.on))


"""
# When a variable is used inside a class by its instance is known as data Attribute python
    (fields in JAVA and data members in C++).
# NOTE : IN PYTHON EVERY TYPE IS A CLASS.
        In Python classes are dynamic in nature i.e. we can add attribute whenever we want,
        but this attribute will only be available to the instance which is using it.
    
"""
kenwood.power = 18.7
print(kenwood.power)
# print(hamilton.power)        O/P-> Error
print("Line-42  " * 50)

print(Kettle.power_source)
print(kenwood.power_source)
kenwood.power_source += " FUCKS!"  # But this creates a new member in local to the method as we are assigning
print(kenwood.power_source)
print(hamilton.power_source)

# power_source is just like member variable
# O/P->
# electricity
# electricity
# electricity FUCKS!
# electricity
# But if we write: we will observe O/P changes it is because we are making changes through class
Kettle.power_source += "FUCKS!"
print(kenwood.power_source)
print(hamilton.power_source)

# we can print namespace of each instance and a class using __dict__
# power_source is somewhat like a static member, we can see in the O/P below namespace of class contains the variable
# while the objects do not have it
# if change the value of the power_source in Class then object's will also be changed

print(kenwood.__dict__)
print(hamilton.__dict__)
print(Kettle.__dict__)
""" O/P:
{'make': 'Kenwood', 'price': 20.9, 'on': True, 'power': 18.7, 'power_source': 'electricity FUCKS!'}
{'make': 'HAMILTON', 'price': 67.3, 'on': False}
{'__module__': '__main__', 'power_source': 'electricityFUCKS!', '__init__': <function Kettle.__init__ at 0x03734150>, 
'switch_on': <function Kettle.switch_on at 0x03734108>, '__dict__': <attribute '__dict__' of 'Kettle' objects>, 
'__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__': None}
"""
