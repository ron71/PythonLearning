# Place Geometry Manager:

# Its is more feasible to use that Pack Geometry Manager
# It works by specifying absolute position of at least one window or windows
# that can be positioned relative to another window
# Unless we know the screen size the use of absolute positioning is not recommended.
# So its better to use Grid Geometry Manger

# Grid Geometry Manger:
# In this layout dimensions of the widget are automatically calculated.
# For instance, widgets in same column can be aligned below each other and
# row can be aligned next to each other.
# It just like placing windows in matrix

try:
    import tkinter
except:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("GRID GEOMETRY DEMO")
mainWindow.geometry('640x480+100+100')

label = tkinter.Label(text='GRID MANAGER')
label.grid(column= 0, row=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(column=0, row = 1)


canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.grid(column=0,row=1)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(column=1, row=1, sticky='N')
# note: Here 'sticky' tag is used as same as anchor tag

button1 = tkinter.Button(rightFrame, text='Button 1')
button1.grid(column=0, row=0, sticky='N')

button2 = tkinter.Button(rightFrame, text='Button 2')
button2.grid(column=0, row=1, sticky='N')

button3= tkinter.Button(rightFrame, text='Button 3')
button3.grid(column=0, row=2, sticky='N')

button4 = tkinter.Button(rightFrame, text='Button 4')
button4.grid(column=0, row=3, sticky='N')

# help(label.grid)
#
# grid_configure(cnf={}, **kw) method of tkinter.Label instance
# Position a widget in the parent widget in a grid.
# Use as options:
#   column=number - use cell identified with given column (starting with 0)
#   columnspan=number - this widget will span several columns
#   in=master - use master to contain this widget
#   in_=master - see 'in' option description
#   ipadx=amount - add internal padding in x direction
#   ipady=amount - add internal padding in y direction
#   padx=amount - add padding in x direction
#   pady=amount - add padding in y direction
#   row=number - use cell identified with given row (starting with 0)
#   rowspan=number - this widget will span several rows
#   sticky=NSEW - if cell is larger on which sides will this widget stick to the cell boundary

# columnconfigure() Or grid_columnfigure()
# By default columns become of same size of the widgets
# So we can override this method to configure our columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(1, weight=1)

# NOTE: 'sticky' attr will opnly ork if weight is provided
# We can also see the borders of the frame just like Canvas
leftFrame.config(relief='sunken', borderwidth=4)
leftFrame.grid(sticky='ns')
rightFrame.config(relief='sunken', borderwidth= 4)
rightFrame.grid(sticky='new') # north|east|west
rightFrame.columnconfigure(0, weight=1)
rightFrame.columnconfigure(1, weight=1)
rightFrame.columnconfigure(2, weight=1)
rightFrame.columnconfigure(3, weight=1)

button1.grid(sticky='ew')
button2.grid(sticky='we')
button3.grid(sticky='ew')
button4.grid(sticky='ew')

mainWindow.mainloop()