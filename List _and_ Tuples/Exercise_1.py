# Exercise 12.1
# A magic 8-ball, when asked a question, provides a random answer from a
# list. The code below contains a list of possible answers. Create a magic 8-ball program that
# asks a question, then gives a random answer.
import random
answers = ["It is certain", "It is decidedly so", "Without a doubt",
           "Yes, definitely", "You may rely on it", "As I see it,yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy try again", "Ask again later", "Better not tell you now",
            "Cannot predict now", "Concentrate and ask again", "Don't count on it",
            "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
quitOptions = ['quit', 'bye', 'fuck you', 'see ya']
while True:
    question = input("Hey! Ask me anything").lower()
    for word in quitOptions:
        if word in question:
            print('I better not talk to you, Bye!')
            question = "quit"
            break
    if question == 'quit':
        break
    print(answers[random.randint(0,len(answers))])