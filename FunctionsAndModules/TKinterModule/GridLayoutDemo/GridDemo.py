# in this we trey to make the layout of tof the window as the picture

try:
    import tkinter
except:
    import Tkinter as tkinter

import os
import os.path
mainWindow = tkinter.Tk()
mainWindow.title("GRID DEMO")
mainWindow.geometry("640x480+50+50")
label = tkinter.Label(text = 'Tkinter Grid Demo')
label.grid(column='0',row=0, sticky='n', columnspan=3)
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=500)
# Weight  means when we resize the window, then this column decreases/increases 'n' times faster the one times.
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=100)
mainWindow.rowconfigure(2,weight=60)
mainWindow.rowconfigure(3,weight=1)
mainWindow.rowconfigure(4,weight=1)
mainWindow['padx'] = 8
mainWindow['pady'] = 8

# Now adding a List box using widget "Listbox"
fileList = tkinter.Listbox(mainWindow, relief='sunken', borderwidth=4)
fileList.grid(column= 0, row=1,rowspan=2, sticky= 'news',)
# Adding item in Listbox
# we can list out the folders in folder

for zone in os.listdir('C:\Windows\System32'):
    zoneCompletePath = "C:\Windows\System32\\" + str(zone)
    if os.path.isdir(zoneCompletePath):
        fileList.insert(tkinter.END, zone)
        # insert(position, item) position states where to insert the item in the list
        # NOTE: If we pass '0' as position items will added at the top of the list

# Adding ScrollBar
scrollBar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
# 'orient' specifies the vertical or horizontal scrolling
# 'command' specifies the which list ie to be scrolled and 'yview' specifies to move the fileList in verticle direction
# while scrolling
scrollBar.grid(column=1, row=1, rowspan=2, sticky='wns',)
# Now if we scroll using mouse middle scroller we will observe the scrollBar do not moves, so we can fix this As:
fileList['yscrollcommand'] = scrollBar.set
# for horizontal use 'xscrollcommand'


# Adding File details Frame using LabelFrame
fileDetailsFrame = tkinter.LabelFrame(mainWindow, text='File Details', relief='groove', borderwidth=2)
fileDetailsFrame.grid(column=2, row=1, sticky='ne')
# For Radio Buttons in it
rbOption = tkinter.IntVar() # here we assigned one variable for all three radio buttons
# so that only can be selected at a time
rbOption.set(2)        # We set default value of rebOption as 2
# Creating RadioButtons
radio1 = tkinter.Radiobutton(fileDetailsFrame,text='Filename', variable=rbOption, value=1)
# variable--> it is the variable which we have assigned for the value via method: get()
# value is just like key for each radio button which will be stored in rbOption
radio2 = tkinter.Radiobutton(fileDetailsFrame, text='Path', variable=rbOption, value=2)
radio3 = tkinter.Radiobutton(fileDetailsFrame, text='TimeStamp', variable=rbOption, value=3)
radio1.grid(column=0, row=0, sticky='nws')
radio2.grid(column=0, row=1, sticky='nws')
radio3.grid(column=0, row=2, sticky='nws')

# We wante to show the file name, path, timestamp whichever is selected, So we will add a label name "Result" and
# a Entry widget to print the result in it. Its like TextField
resultLabel = tkinter.Label(mainWindow, text='Result :')
resultLabel.grid(column=2, row=2, sticky='nw')
resultEntry = tkinter.Entry(mainWindow)
resultEntry.grid(column=2, row=2, sticky='sw')

# Adding Time Frame using LabelFrame
timeFrame = tkinter.LabelFrame(mainWindow, text='Time', relief='groove', borderwidth=1)
timeFrame.grid(column=0, row=3, sticky='nwe')

# Adding Combolist
checkList1 = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0,24)))
checkList1.grid(column=0, row=0, sticky='es', pady=5)
checkList2 = tkinter.Spinbox(timeFrame, width=2, value= tuple(range(0,60)))
checkList2.grid(column=1, row=0, sticky='s', pady=5)
checkList3 = tkinter.Spinbox(timeFrame, width=2, value= tuple(range(0,60)))
checkList3.grid(column=2, row=0, sticky='ws', pady=5)
timeFrame.columnconfigure(0, weight=2)
timeFrame.columnconfigure(1, weight=1)
timeFrame.columnconfigure(2, weight=2)
timeFrame.rowconfigure(0, weight=1)

# Adding DateFrame
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(column=0, row=4, sticky='nwe')
dateFrame.columnconfigure(0, weight=1)
dateFrame.columnconfigure(1, weight=1)
dateFrame.columnconfigure(2, weight=1)
dateFrame.rowconfigure(0, weight=1)
dateFrame.rowconfigure(1, weight=1)

dayLabel = tkinter.Label(dateFrame, text='Day')
dayLabel.grid(column=0, row=0, sticky='s')
monthLabel = tkinter.Label(dateFrame,text='Month')
monthLabel.grid(column=1, row=0, sticky='s')
yearLabel = tkinter.Label(dateFrame, text='Year')
yearLabel.grid(column=2, row=0, sticky='s')

daySpinner = tkinter.Spinbox(dateFrame, width=4, value=tuple(range(1,32)))
daySpinner.grid(column=0, row=1, sticky='n',)
monthSpinner = tkinter.Spinbox(dateFrame, width=4, value=('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JULY', 'AUG',
                                                          'SEP', 'OCT', 'NOV', 'DEC'))
monthSpinner.grid(column=1, row=1, sticky='n')
yearSpinner = tkinter.Spinbox(dateFrame, width=4, value=tuple(range(1990, 2021)))
yearSpinner.grid(column=2, row=1, sticky='n')

# Adding Ok Button
okButton = tkinter.Button(text='OK', width=6)
okButton.grid(column=3, row=4, sticky='e')
# Adding the cancel Button
cancelButton = tkinter.Button(text='cancel', width=8)
cancelButton.grid(column=4, row=4, sticky='w')

mainWindow.mainloop()

