# TK inter is a built module for Gui based methods and programming.
# it provides widget toolkit for GUI
# TK tool kit wal developed to work with scripting language 'TCL'
# Python binds the code in TCL code which is ran by TCL interpreter
# How ever This interpreter is embedded in python, so no need for extra installation
# Its documentation is not so good
# For Documentation : http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#                     https://tkdocs.com/index.html
# if we aork in python 2 the module name is 'Tkinter'
# using 'tkinter' will fail to run on python 2
# so using exception handling can work for us

try:
    import tkinter
except ImportError:     # For Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test() # it provides a test templete to check

# To run tkinter window

mainWindow = tkinter.Tk() # Created object of tk class
mainWindow.title("Tkinter DEMO WINDOW") # To Provide title to layout window
mainWindow.geometry("640x640+80+100")          # To provide dimension to layout window
# geomerty(str) method takes one argument as String.
# This String contains dimensions in pixels separated by 'x' and
# x,y co-ordinates for the position of the layout for top-left
# Coordinates are separated by '+' or "-" sign
# '-' sign denotes from right for x coordinate and from bottom for y coordinate

# Now we must pass the control  to Tk object (in this case, mainWidow) to run it by mainLoop function
mainWindow.mainloop()

# Note ; Everything in tk is a window. Objects are placed in hierarchy.
# Here mainWindow is root window, so everything is to placed in within it or one of the child window.
# Note : Not every window can have children.
# Every Window except root window, must have master window.