from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks += 1
    buttonText.set('Clicks {}'.format(clicks))

def click_button_int():
    click.set(click.get() + 1)
    

root = Tk()
root.title("Graphics Python")
root.geometry("400x300")

buttonText = StringVar()
buttonText.set('Clicks {}'.format(clicks))

click = IntVar()
click.set(0)

btn = Button(root,
             textvariable=click,
             background='#555',
             foreground='#ccc',
             font='16',
             bd='5',
             command=click_button_int)
btn.pack()


root.mainloop()


