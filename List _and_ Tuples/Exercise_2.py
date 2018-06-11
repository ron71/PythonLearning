# Exercise 12.2
# A playing card consists of a suit ("Hearts", "Spades", "Clubs","Diamonds") and a
# value (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King","Ace").
# Create a list of all possible playing cards, which is a deck. Then create a function
# that shuffles the deck, producing a random order.
import random
suitList = ["Hearts", "Spades", "Clubs","Diamonds"]
valueList = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King","Ace"]
deck = list()

for suit in suitList:
    for value in valueList:
        deck.append([suit, value])


check = []
while len(check) != len(deck):
    i = random.randint(0, len(deck)-1)
    if i not in check:
        check.append(i)
        print(deck[i])

