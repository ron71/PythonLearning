try:
    import tkinter
except:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.geometry("280x400+100+100")
mainWindowPadding=8
mainWindow.title("Calculator")
result = tkinter.Entry(mainWindow)
result.grid(column=0,row=0,sticky="news", pady=8)
mainWindow['padx']=mainWindowPadding

keys=[[['C', 1],['CE', 1]],
      [['7', 1],['8', 1],['9', 1],['*', 1]],
      [['6', 1],['5', 1],['4', 1],['/', 1]],
      [['1', 1],['2', 1],['3', 1],['+', 1]],
      [['.', 1],['0', 1],['=', 1],['-', 1]]
      ]


keypads = tkinter.Frame(mainWindow)
keypads.grid(column=0, row=1)
buttonPad = list()
roW = 0
for keyStrip in keys:
    col = 0
    for key in keyStrip:
        button = tkinter.Button(keypads, text=key[0], width=8,height=2)
        button.grid(column=col, row=roW,columnspan=key[1], padx=2, pady=2)
        buttonPad.append(button)
        col+=1
    roW+=1

# NOw we can set the min and the maximum size of the mainWindow
mainWindow.update()
# update() makes the window to wait till above written setups are set in the window
# so that the width or any other information caan be fetched
mainWindow.minsize(mainWindowPadding*2+keypads.winfo_width(), 17+result.winfo_height()+keypads.winfo_height())
mainWindow.maxsize(mainWindowPadding*2+keypads.winfo_width(), 17+result.winfo_height()+keypads.winfo_height())
# winfo_width() returns the width of the widget set on window

mainWindow.mainloop()