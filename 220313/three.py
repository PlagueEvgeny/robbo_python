from tkinter import *

clicks = 0

def click():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))

root = Tk()
root.title('GUI in Python')
root.geometry("300x250")
btn1 = Button(text='CLICK ME', background='#555', foreground='#ccc',
              padx='15', pady='6', font='15')

btn1.pack(side=TOP)

btn2 = Button(text='CLICK ME', background='#555', foreground='#ccc',
              padx='15', pady='6', font='15')

btn2.pack(side=BOTTOM)

btn3 = Button(text='CLICK ME', background='#555', foreground='#ccc',
              padx='15', pady='6', font='15')

btn3.pack(side=RIGHT)

btn4 = Button(text='CLICK ME', background='#555', foreground='#ccc',
              padx='15', pady='6', font='15')

btn4.pack(side=LEFT)

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
root.mainloop()
