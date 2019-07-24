from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk




def newFile(event=None):
    window.title("Untitled")
    global file_name
    file_name = None
    content.delete(1.0, END)


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

def changeFont():
    content["font"]=fontVar+" "+str(sizeVar)+" "+typeVar



def fontChanged(event):
    global fontVar
    fontVar=event.widget.get(ANCHOR)
    changeFont()

def sizeChanged(event):
    global sizeVar
    sizeVar = event.widget.get(ANCHOR)
    changeFont()


def typeChanged(event):
    global typeVar
    typeVar=event.widget.get()
    changeFont()


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

    fontBox.bind("<<ListboxSelect>>",fontChanged)
    sizeBox.bind("<<SizeBoxSelect>>",sizeChanged)
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
window.geometry('500x400')
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="NewFile",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close",command=closeWindow)



editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_command(label="Option",command=optionClick)
content=Text(window)
content.place(width=500,height=400)

mainMenu.add_command(label="View")
mainMenu.add_command(label="Help")

window.mainloop()