from tkinter import *
window=Tk()
mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close")

mainMenu.add_command(label="Help")

content=Text(window,width=100)
window.mainloop()