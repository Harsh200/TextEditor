from tkinter import *
from tkinter import filedialog

def saveFile():
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    textuserwrote=str(content.get(1.0,END))
    f.write(textuserwrote)
    f.close()


def openFile():
    t=filedialog.askopenfile(mode="r",title="Select FIle",
                             filetypes=[("All Files","*.*")])
    content.insert(END,t.read())
    t.close()

def closeWindow():
    window.destroy()


window=Tk()
mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close",command=closeWindow)

mainMenu.add_command(label="Help")

content=Text(window,width=100)
content.grid(row=0,column=0,padx=5,pady=5)
window.mainloop()