from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

base = Tk()
width = 800
height = 600

textArea = Text(base,wrap= WORD)
menuBar = Menu(base)
fileMenu = Menu(menuBar,tearoff=0)
editMenu = Menu(menuBar,tearoff=0)
exitMenu = Menu(menuBar,tearoff=0)
formatMenu = Menu(menuBar,tearoff=0)
helpMenu = Menu(menuBar,tearoff=0)

scrollBarRight = Scrollbar(textArea)
# scrollBarBottom = Scrollbar(textArea, orient='horizontal')



file = None
mode = 'Light'
font = 'Courier'
fsize = 14
base.title('Untitled - Notepad')

screenWidth = base.winfo_screenwidth()
screenHeight = base.winfo_screenheight()

# For left-alling
left = (screenWidth / 2) - (width / 2)

# For right-allign
top = (screenHeight / 2) - (height / 2)

# For top and bottom
base.geometry('%dx%d+%d+%d' % (width,height, left, top))
# base.geometry(f"{width}x{height}")
#For resize
base.grid_rowconfigure(0,weight=1)
base.grid_columnconfigure(0,weight=1)

#Controls
textArea.grid(sticky = N + E + S + W)
textArea.config(font= (font,fsize))

def newFile(event=''):
    base.title('Untitled - Notepad')
    file = None
    textArea.delete(1.0,END)

def openFile(event=''):
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        base.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        file1 = open(file, "r")
        textArea.insert(1.0, file1.read())
        file1.close()


def saveFile(event=''):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            file1 = open(file, "w")
            file1.write(textArea.get(1.0, END))
            file1.close()
            base.title(os.path.basename(file) + " - Notepad")
    else:
        file = open(file, "w")
        file.write(textArea.get(1.0, END))
        file.close()

def exitFile(event=''):
    base.destroy()

def editCut():
    textArea.event_generate('<<Cut>>')
    textArea.event_generate('<<Cut>>')

def editCopy():
    textArea.event_generate('<<Copy>>')

def editPaste():
    textArea.event_generate('<<Paste>>')

def cntrlf(self, event):
    self.searchbox()

def showAbout():
    showinfo('Notepad','You Can write your text here.!!')

def formatFont():
    topLevel = Toplevel(base)
    topLevel.title("Font")
    topLevel.geometry('500x500')

    lab1 = Label(topLevel,text='Font')
    lab1.place(x=13,y=29)
    e1 = Entry(topLevel)
    e1.insert(0,font)
    e1.place(x=13,y=55)

    listbox = Listbox(topLevel,selectmode=EXTENDED)
    lst = ['Calibri','Cambria','Comic Sans MS','Courier','Gabriola','Georgia','Helvetica','Times New Roman','Verdana']
    for i in sorted(lst):
        listbox.insert(END,i)
    listbox.place(x=13,y=75)
    def CurSelet(evt):
        value = str((listbox.get(listbox.curselection())))
        e1.delete(0, END)
        e1.insert(0,value)

    lab2 = Label(topLevel, text='Font Size')
    lab2.place(x=200, y=29)
    e2 = Entry(topLevel)
    e2.insert(0, str(fsize))
    e2.place(x=200, y=55)
    listbox1 = Listbox(topLevel, selectmode=EXTENDED)
    lst1 = [8,9,10,11,12,14,16,18,20,22,24,26,30,32,34,36,40]
    for i in sorted(lst1):
        listbox1.insert(END, i)
    listbox1.place(x=200, y=75)

    def CurSel(evt):
        value1 = str((listbox1.get(listbox1.curselection())))
        e2.delete(0, END)
        e2.insert(0, value1)

    listbox.bind('<<ListboxSelect>>', CurSelet)
    listbox1.bind('<<ListboxSelect>>', CurSel)



    lab3 = Label(topLevel,text='Mode')
    lab3.place(x=370,y=29)

    radio = StringVar()
    def ok():
        global mode,font,fsize
        mode = radio.get()
        # if mode1==1:
        #     mode = 'Light'
        # else:
        #     mode = 'Dark'

        if mode == 'Light':
            textArea.config(bg='#FFFFFF', fg='#000000',insertbackground='#000000')
        else:
            textArea.config(bg='#282525', fg='#FFFFFF',insertbackground='#FFFFFF')

        font = e1.get()
        print(font)
        fsize = e2.get()
        print(fsize)
        textArea.config(font=(font,fsize))
        topLevel.destroy()

    r1 = Radiobutton(topLevel,text='Light',value='Light',variable=radio)
    r1.place(x=370,y=55)

    r2 = Radiobutton(topLevel,text='Dark',value='Dark',variable=radio)
    r2.place(x=370,y=85)
    if mode=='Light':
        r1.select()
    else:
        r2.select()


    button = Button(topLevel, text="OK",font=('',12), command=ok)
    button.place(x=450,y=450)



    topLevel.mainloop()

# File menu
fileMenu.add_command(label='New                 Ctrl+N',command=newFile)
base.bind('<Control-n>', newFile)
fileMenu.add_command(label='Open               Ctrl+O',command=openFile)
base.bind('<Control-o>', openFile)
fileMenu.add_command(label='Save                 Ctrl+S',command=saveFile)
base.bind('<Control-s>', saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit                  Ctrl+Q',command=exitFile)
base.bind('<Control-q>', exitFile)
menuBar.add_cascade(label='File',menu=fileMenu)

# Edit Menu
editMenu.add_command(label='Cut                  Ctrl+X',command=editCut)
editMenu.add_command(label='Copy               Ctrl+C',command=editCopy)
editMenu.add_command(label='Paste               Ctrl+V',command=editPaste)

# editMenu.add_command(label="Search Ctrl+f", command=cntrlf)
menuBar.add_cascade(label='Edit',menu=editMenu)

# Help Menu
helpMenu.add_command(label='About Notepad',command=showAbout)
menuBar.add_cascade(label='Help',menu=helpMenu)

#Format Menu
formatMenu.add_command(label='Format/Font',command=formatFont)
menuBar.add_cascade(label='Format',menu=formatMenu)
# menuBar.add_cascade(label='Exit',command=exitFile())
base.config(menu = menuBar)

# Scroll Bar Adjust left
scrollBarRight.pack(side=RIGHT, fill=Y)
scrollBarRight.config(command=textArea.yview)
textArea.config(yscrollcommand=scrollBarRight.set)

base.mainloop()