try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(canvas,size):
    for x in range(-size,size):
        y = pow(x,2)/size
        plot_Parabola(canvas,x,y)

    # the plot will be opening downwards altough y is positive.
    # This is because the canvas has scaled the y axis taking negative above the origin.



def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width()/2
    y_origin = canvas.winfo_height()/2
    canvas.configure(scrollregion=(-x_origin,-y_origin,x_origin,y_origin))
    # Scrollregion sets the center of the drawing in center of the given coordinates
    # To create lines we use create_line(x1,y1,x2,y2) method
    canvas.create_line(0,-y_origin,0,y_origin, fill='white')
    canvas.create_line(-x_origin,0,x_origin,0, fill='white')
    print(locals())     # it prints all the local variables
    print(repr(canvas)) # It prints details of the object


def plot_Parabola(canvas, x, y):

    # for i in range(0,x+1):
    canvas.create_line(x,y,(x+1),y+1,fill='black')
    print(repr(canvas))

    # for i in range(0,x+1):
        # canvas.create_line(-x,y,-(x+1),y+1,fill='black')

    # Above will create a line of only one pixel, which is like a dot or point
    # So to resole this we can modify the parabola function as y=x*x/100


mainWindow = tkinter.Tk()
mainWindow.geometry('700x550+100+100')
mainWindow.title("Parabola")
mainWindow.columnconfigure(0,weight=1)
mainWindow.rowconfigure(0,weight=1)

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=3)
canvas.grid(column=0, row=0, sticky='news')



draw_axes(canvas)

parabola(canvas,100)
mainWindow.mainloop()

# Note: Variable which are local to a function cannot be used outside the function
# but a function can use the variable outside the function

