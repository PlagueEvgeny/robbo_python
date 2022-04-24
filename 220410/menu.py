from tkinter import *

root = Tk()
root.title('GUI')


mainmenu = Menu()
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=1)
filemenu.add_command(label='Open')
filemenu.add_command(label='New')
filemenu.add_command(label='Save')
filemenu.add_separator()
filemenu.add_command(label='Exit')

helpmenu = Menu(mainmenu, tearoff=0)

helpmenu2 = Menu(helpmenu, tearoff=0)
helpmenu2.add_command(label='Local Docs')
helpmenu2.add_command(label='My Site')

helpmenu.add_cascade(label='Help', menu=helpmenu2)
helpmenu.add_command(label='About')

mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)

root.mainloop()
