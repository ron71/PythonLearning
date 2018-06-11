#   Example No- 01

# available_direction = {"east","north","south"}
# choose_direction = ""
# while choose_direction not in available_direction:
#     choose_direction = input("CHOOSE CHOOSE THE DIRECTION")
#
# print("GOOD,YOU ARE OUT OF WHILE LOOP\n")

import random

highest = 10

answer = random.randint(1, highest)

print("Please guess a no between 1 and 10")
guess = int(input())
if guess != answer:
    if guess<answer:
        print("Please guess bigger no")
    else:
        print("PLEASE GUESS LOWER NO")
    guess = int(input())
    if(guess == answer):
        print("WELDONE YOU GUESSED RIGHT NO")
    else:
        print("Sorry game over")
else:
    print("WELLDONE YOU GUESSED IT IN 1 GO.")

