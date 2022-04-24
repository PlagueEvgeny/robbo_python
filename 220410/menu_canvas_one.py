from tkinter import *

def circle():
    can.create_oval(
        x,y, x+30, y+34)
    


def square():
    can.create_rectangle(
        x,y, x+30, y+30)
    

def triangle():
    can.create_polygon(x, y, x-15, y+30, x+15, y+30, x+40, y+20,
                       x+10, y+60, fill='blue', outline='black')

def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

    
x = 0
y = 0

root = Tk()
can = Canvas(width=300, height=300, bg='white')
can.pack()
can.bind('<Button-3>', popup)
menu = Menu(tearoff=0)
menu.add_command(label='Круг', command=circle)
menu.add_command(label='Квадрат', command=square)
menu.add_command(label='Треугольник', command=triangle)

root.mainloop()




