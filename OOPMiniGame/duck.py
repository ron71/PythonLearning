""" Python doesn't support method overloading. However it can be achieved by providing name
    arguments having some default values.
    Polymorphism - same name but different parameter list. In python there are no check for types of the arguments unless
    they are in use. So we can not say that polymorphism exists in Python.
    For Example:
    a = 'Hello'
    b = 3
    c = 1,2,3

    print(a)
    print(b)
    print(c)

    We will observe print is working and has different arguments. It can be said that it is a kind of polymorphism.
    Well fact is that int, String, tuple all are inherited from a single class 'Object'. And they all implement object's
    method named __str__() which return the printable content of these data type values.
    """


class Wing(object):
    """We have made this class to illustrate the concept of comprehension."""
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("I am born to fly.")
        elif self.ratio == 1:
            print("I'm not a pro but I can fly")
        else:
            print("I should better walk.")


class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print('Come on in, water is so lovely.')

    def quack(self):
        print('quack, quack, quack!')

# *************Concept of Composition*********************
    # It creates 'Has a relationship'
    def __init__(self, ratio):
        self._wing = Wing(ratio)
        # We are storing wing object as data attribute this is called composition.

    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("Waddle, waddle, I waddle too!")

    def swim(self):
        print('Come on in, water is so lovely but its chilled out here.')

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin.")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    #     donald = Duck()
    #     test_duck(donald)
    #
    #     percy = Penguin()
    #     test_duck(percy)
    #
    # """ We can see that test_duck is working with penguin too.
    # It is because Python doesn't cares which class it is unless the attributes mentioned are in that particular Class
    # If penguin can pass the test_duck then are the duck.
    # That means many forms exists, therefore Polymorphism established at some extent considering the test_duck method.
    #
    # NOTE: Inheritance establishes 'IS A' relationship."""

    # **************************Concept of Composition*********************************************
    donald = Duck(0.2)
    donald.fly()