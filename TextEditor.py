from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk




def saveFile():
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    try:
        textuserwrote=str(content.get(1.0,END))
        f.write(textuserwrote)
    except:
        print("Cannot Save the file")
    finally:
        f.close()


def openFile():
    try:
        t=filedialog.askopenfile(mode="r",title="Select FIle",
                             filetypes=[("All Files","*.*")])
        content.insert(END,t.read())
    except:
        print("Cannot Load the file")
    finally:
        if t:
            t.close()

def closeWindow():
    window.destroy()

def fontChanged(event):
    global fontVar
    fontVar=event.widget.get(ANCHOR)
    changeFont()

def sizeChanged(event):





def optionClick():
    optionWindow=Tk()
    lbfont=Label(optionWindow,text="Font")
    lbsize = Label(optionWindow, text="Size")
    lbtype = Label(optionWindow, text="Type")
    fontBox=Listbox(optionWindow)
    for f in font.families():
        fontBox.insert(END,f)

    sizeBox=Listbox(optionWindow)
    for i in range(8,88,4):
        sizeBox.insert(END,i)
    typeOption=("normal","bold","normal italic","bold italic")
    cbxType=ttk.Combobox(optionWindow,values=typeOption)
    cbxType.set("normal")

    fontBox.bind("<<ListboxSelected>>",fontChanged)
    sizeBox.bind("<<SizeBoxSelected>>",sizeChanged)
    cbxType.bind("<<ComboboxSelected>>",typeChanged)

    lbfont.grid(row=0,column=0,padx=10,pady=5)
    lbsize.grid(row=0, column=1, padx=10, pady=5)
    lbtype.grid(row=0, column=2, padx=10, pady=5)
    fontBox.grid(row=1,column=0,padx=10,pady=5)
    sizeBox.grid(row=1,column=1,padx=10,pady=5)
    cbxType.grid(row=1,column=2,padx=10,pady=5)
    optionWindow.mainloop()




window=Tk()
fontVar="Ariel"
sizeVar=11
typeVar="normal"


mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close",command=closeWindow)

mainMenu.add_command(label="Help")

editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_command(label="Option",command=optionClick)
content=Text(window,width=100)
content.grid(row=0,column=0,padx=5,pady=5)


window.mainloop()