from tkinter import *
window=Tk()
mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)

window.mainloop()