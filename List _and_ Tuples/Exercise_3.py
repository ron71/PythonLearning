# Exercise 12.3
# A first-in-first-out (FIFO) structure, also called a “queue,” is a list that gets new elements added at the end,
# while elements from the front are removed and processed. Write a program that processes a queue.
# In a loop, ask the user for input. If the user just presses the Enter key, the program ends.
# If the user enters anything else, except for a single question mark (?),
# the program considers what the user entered a new element and appends it to the queue.
# If the user enters a single question mark, the program pops the first element from the queue and displays it.
# You have to take into account that the user might type a question mark even if the queue is empty.

queue = list()

while True:
    element = input("ENTER THE ELEMENT TO BE INSERTED\t")
    if element == '':
        break
    elif element == "?":
        if len(queue) != 0:
            print('Popped Element : {}'.format(queue.pop(0)))
        else:
            print('Queue is empty')
    else:
        queue.append(element)
        print("Element inserted in Queue successfully")
