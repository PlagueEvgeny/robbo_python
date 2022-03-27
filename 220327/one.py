from tkinter import *
from tkinter import messagebox

def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    message_entry.delete(0, END)
          

def display():
   messagebox.showinfo("GUI Python", name.get() + " " + surname.get() + "\n" + message.get())

root = Tk()
root.title("GUI")
root.geometry("400x400")

name = StringVar()
surname = StringVar()
message = StringVar()
ismarried = IntVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
message_label = Label(text="Сообщение")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
message_label.grid(row=2, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
message_entry = Entry(textvariable=message)

name_entry.grid(row=0, column=1 , padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
message_entry.grid(row=2, column=1, padx=5, pady=5)

name_entry.insert(0, "Tom")
surname_entry.insert(0, "Soyer")
message_entry.insert(0, "One of the main characters in Mark Twains novels")

info = Button(text="DISPLAY", command=display)
clear = Button(text="CLEAR", command=clear)
ismarried_checkbutton = Checkbutton(text='Gud/No gud', variable=ismarried)
ismarried_checkbutton.grid(row=4, column=1, padx=5, pady=5)

ismarried_label = Label(textvariable=ismarried)
ismarried_label.grid(row=4, column=0, padx=5, pady=5)

info.grid(row=3, column=1, padx=5, pady=5, sticky="e")
clear.grid(row=3, column=0, padx=5, pady=5, sticky='e')

root.mainloop()






