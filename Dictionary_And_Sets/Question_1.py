# Exercise 14.1
#  A famous syllogism says: All men are mortal. Socrates is a man. Therefore
# Socrates is mortal. In the code block below you see some sets. The first is the set of all things
# (I know a few are missing, but for the sake of argument). The second is the set of all men
# (assuming that the first set indeed contains all things). The third set contains everything
# that is mortal (again, assuming...). Using set operators and methods, show that indeed
# (a) all men are mortal,
# (b) Socrates is a man, and
# (c) Socrates is mortal. Also shows that
# (d) there are mortal things that are not men, and
# (e) there are things that are not mortal.

allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera",
             "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates", "Plato", "Eratosthenes", "Cat", "Dog"}


if men.issubset(mortalthings):
    print("All men are mortal")

if "Socrates" in men.intersection(mortalthings):
    print("Socrates is a man, and Socrates is mortal")

if len(mortalthings.difference(men))>0:
    print('there are mortal things that are not men')

if len(allthings.difference(mortalthings))>0:
    print('there are things that are not mortal.')
