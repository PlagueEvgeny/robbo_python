import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

    __root = Tk()
    # ширина и высота окна по умолчанию
    __thisWidth = 300
    __thisHeight = 300
    # Компоненты
    __thisTitle = "Notepad"
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)

    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisButtonMenu = Menu(__root, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    

    def __init__(self, **kwargs):
        try:
            self.__root.wn_iconbitmap('')

        except:
            pass

        try:
            self.__thisWidth = kwargs['width']

        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']

        except KeyError:
            pass


        self.__root.title(self.__thisTitle)

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()


        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d%d%d' % (self.__thisWidth, self.__thisHeight,
                                            left, top))


        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)


        self.__thisTextArea.grid(sticky = N + E + S + W)


        self.__thisFileMenu.add_command(label="New", command=self.__newFile)

        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)

        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

        self.__thisFileMenu.add_separator()

        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApp)


        self.__thisMenuBar.add_cascade(label='File', menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label='Cut', command=self.__cut)

        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)

        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)

        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)

        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__thisButtonMenu.add_command(label='cut', command=self.__cut)
        self.__thisButtonMenu.add_command(label='copy', command=self.__copy)
        self.__thisButtonMenu.add_command(label='paste', command=self.__paste)

        self.__root.config(menu=self.__thisMenuBar)


        self.__thisScrollBar.pack(side=RIGHT, fill=Y)


        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        self.__thisTextArea.bind("<Control-Key-a>", self.__all_select)
        self.__thisTextArea.bind("<Control-Key-A>", self.__all_select)
        self.__root.bind("<Button-3>", self.__showMenu)


    def __quitApp(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad 0.1v", 'My notepad')
    
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Document", "*.txt"),
                                                 ("Python Code", "*.py"),
                                                 ("JavaScript Code", "*.js")
                                                 ])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + f' - {self.__thisTitle}')
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__root.title(self.__thisTitle)
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Document", "*.txt"),
                                                 ("Python Code", "*.py"),
                                                 ("JavaScript Code", "*.js")
                                                 ])
            if  self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + f' - {self.__thisTitle}')
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __all_select(self, event):
        self.__thisTextArea.tag_add(SEL, '1.0', END)
        self.__thisTextArea.mark_set(INSERT, "1.0")
        self.__thisTextArea.see(INSERT)
        return 'break'

    def __showMenu(self, e):
        self.__thisButtonMenu.post(e.x_root, e.y_root)

    def run(self):
        self.__root.mainloop()

def main():
    notepad = Notepad(width=600,height=400)
    notepad.run()


if __name__ == '__main__':
    main()

        
        
