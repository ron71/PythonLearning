# Packing geometry is suitable for simple Layouts

# CODE NO : 1

# try:
#     import tkinter
# except ImportError:
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
# mainWindow.title("PACK GEOMETRY DEMO")
# mainWindow.geometry('500x500+100+100')
#
# # creating label
# label = tkinter.Label(mainWindow, text='Pack Geometry')
# # Adding label in mainWindow
# label.pack(side='top')
#
# # help(label.pack)
#
# # Options or arguments used in pack():
#
# #     after=widget - pack it after you have packed widget
# #     anchor=NSEW (or subset) - position widget according to
# #                               given direction
# #     before=widget - pack it before you will pack widget
# #     expand=bool - expand widget if parent size grows
# #     fill=NONE or X or Y or BOTH - fill widget if widget grows
# #     in=master - use master to contain this widget
# #     in_=master - see 'in' option description
# #     ipadx=amount - add internal padding in x direction
# #     ipady=amount - add internal padding in y direction
# #     padx=amount - add padding in x direction
# #     pady=amount - add padding in y direction
# #     side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
#
# # Creating Canvas
#
# canvas = tkinter.Canvas(mainWindow, relief= 'raised', borderwidth=2)
# # relief option will raise the canvas.
# # Adding Canvas
# canvas.pack(side= 'left', fill=tkinter.Y, expand=True)
#
# # we can fill the canvas to match the parent size by using --. fill= tkinter.Y or X or BOTH
# # NOTE : if we only use fill= tkinter.X to stretch i horizontal direction it won't work
# # We have to use one extra option i.e. expand=True
#
# button1 = tkinter.Button(mainWindow, text='CLICK')
# button1.pack(side='left', anchor='n') # By default-->  side='top'
# # Button will be left side of canvas in north direction taking mainWindow's center as reference
# button2 = tkinter.Button(mainWindow, text='CLICK')
# button2.pack(side='left', anchor='s')
# # Button2 will be left of Button1 and in South from center
# button3 = tkinter.Button(mainWindow, text='CLICK')
# button3.pack(side='left', anchor='e')
# # Button3 will be left of Button2 and in East from center
# button4 = tkinter.Button(mainWindow, text='CLICK')
# button4.pack(side='right', anchor='w')
# # Button4 will be left of Button3 and in west from center
# mainWindow.mainloop()

# CODE NO-2

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("PACK GEOMETRY DEMO2")
mainWindow.geometry('640x280+100+100')

# creating label
label = tkinter.Label(mainWindow, text='Pack Geometry')
# Adding label in mainWindow
label.pack(side='top')

# Creating a WindowFrame

leftFrame = tkinter.Frame(mainWindow)
# Adding Frame
leftFrame.pack(side='left', fill=tkinter.Y)

canvas = tkinter.Canvas(leftFrame, relief= 'raised', borderwidth=2)
canvas.pack(side='top', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right',  anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='Btn1')
button1.pack(side='top')

button2 = tkinter.Button(rightFrame, text='Btn2')
button2.pack(side='left')
button3 = tkinter.Button(rightFrame, text='Btn3')
button3.pack(side='right' ,anchor='e')
button4 = tkinter.Button(rightFrame, text='Btn4')
button4.pack(side='top')

mainWindow.mainloop()