import math

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.geometry("500x500+100+100")

mainWindow.title("Circle")


def circle_with_center_at_origin(page, radius):
    for i in range(36000):
        # Increasing the range and decreasing the i value inside
        # loop can increase resolution
        i/=100
        x = (math.cos(i))*radius
        y = (math.sin(i))*radius
        plot_Circle(page,x,y)


def circle(page, radius, origin_X, origin_Y):
    for i in range(360):
        x = (math.cos(i))*radius + origin_X
        y = (math.sin(i))*radius + origin_Y
        plot_Circle(page,x,y)


def plot_Circle(page, x,y):
    page.create_line(x,y,x+1,y+1,fill='black')


def drawAxes(canvas):
    canvas.update()
    x_axis = canvas.winfo_width()/2
    y_axis = canvas.winfo_height()/2

    canvas.configure(scrollregion=(-x_axis,-y_axis,x_axis,y_axis))
    canvas.create_line(0,-y_axis,0,y_axis, fill='White')
    canvas.create_line(-x_axis,0,x_axis,0, fill='White')


canvas = tkinter.Canvas(mainWindow,  relief="groove", borderwidth=2)
canvas.grid(column=0, row=0,sticky='news')
mainWindow.columnconfigure(0,weight=1)
mainWindow.rowconfigure(0,weight=1)

drawAxes(canvas)

circle(canvas,40,40,40)


circle_with_center_at_origin(canvas,300)
# for i in range(300):
#     circle(canvas,i)


# Note: We can use oval function of canvas class too
tkinter.Canvas.create_oval(canvas,50,50,-50,-50, outline='red')
tkinter.Canvas.create_oval(canvas,50,50,-50,-79, outline='blue')
mainWindow.mainloop()

