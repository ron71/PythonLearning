import random

highest_limit = 10
answer = random.randint(1, highest_limit)

guessed_answer = ""
guessed_answer = int(input("Please choose a no between 1 to 10 "))

if guessed_answer != answer:
    attempts = 1
    while guessed_answer != answer:
        if guessed_answer == 0:
            attempts = 0
            break
        attempts += 1
        if guessed_answer < answer:
            print("Please choose bigger no or press zero to exit")
        else:
            print("Please choose smaller no or press zero to exit")
        guessed_answer = int(input())
    if attempts == 0:
        print("GAME OVER")
    else:
        print("Well done, you did it in {} attempts ".format(attempts))
else:
    print("WOW, YOU MADE IT IN JUST ONE ATTEMPT")

