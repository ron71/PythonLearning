# Any method in a module is static that mean it must be called with class name IF THE WHOLE MODULE IS IMPORTED
# Turtle Module provides functions of LOGO where we direct the turtle using commands
import turtle
# import time
# Moving forward
print(help(turtle.forward))
print(turtle.heading)
print(turtle.circle)

turtle.forward(150)
turtle.right(60)
print(help(turtle.right))
print(turtle.heading())
turtle.forward(150)
turtle.right(60)
turtle.forward(150)
turtle.right(60)
turtle.forward(150)
turtle.right(60)
turtle.forward(150)
turtle.right(60)
turtle.forward(150)

for i in range(0,360):
    turtle.forward(2)
    turtle.right(1)



# We can also import only the functions which we want in our program using 'from' keyword
# Example:
# from turtle import forward, right, done
# NOTE : Now we don't need to call the method using class name we can call the method just by calling it by its name
# Important: we must import either whole module or each mrthod we gonna use in the code
# now if we run it we will observe that the drawing screen wipes out after completion of program
# so to prevent so, we import another module name 'time' and use its sleep function

# time.sleep(4)
# Another way to restrain the output screen of turtle is to use done() method
turtle.done()
# It will close only if we close it manually
