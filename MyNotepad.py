from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk
from datetime import datetime
import webbrowser


def new_window():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Ahmad Notepad')

    menubar = Menu(root)

    file = Menu(menubar, tearoff=0)
    file.add_command(label="new", command=new)
    file.add_command(label="new_window", command=new_window)
    file.add_command(label="open", command=open)
    file.add_command(label="save", command=save)
    file.add_separator()
    file.add_command(label="exit", command=exit)
    menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))

    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="undo", accelerator="Ctrl+Z", command=undo)
    edit.add_command(label="cut", accelerator="Ctrl+X", command=cut)
    edit.add_command(label="copy", accelerator="Ctrl+C", command=copy)
    edit.add_command(label="paste", accelerator="Ctrl+V", command=paste)
    edit.add_command(label="delete", accelerator="Del", command=delete)
    edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
    edit.add_command(label="Time/Date", accelerator="F5", command=time)
    menubar.add_cascade(label="Edit", menu=edit)

    Format = Menu(menubar, tearoff=0)
    Format.add_command(label="Word Wrap")
    Format.add_command(label="Font...", command=fonts)
    menubar.add_cascade(label="Format", menu=Format)

    Help = Menu(menubar, tearoff=0)
    Help.add_command(label="View Help")
    Help.add_command(label="Send feedback")
    Help.add_command(label="About notepad")
    menubar.add_cascade(label="Help", menu=Help)
    root.config(menu=menubar)

    text = ScrolledText(root, width=1000, height=1000)
    text.place(x=0, y=0)
    root.mainloop()

def open():
    root.filename = filedialog.askopenfilename(initialdir='/', title="select file", filetypes=(("jpeg files",
                                                                                                "*.jpg"),
                                                                                            "all files", '*.*'))
    file = open(root.filename)
    text.insert('end', file.read())

def new():
    text.delete("1.0", "end")


def save():
    root.filename = filedialog.asksaveasfile(mode="w", defaultextension=".text")
    if root.filename is None:
        return
    file_save = str(text.get(1.0, END))
    root.filename.write(file_save)
    root.filename.close()

    def exit():
        message = messagebox.askquestion("Notepad", "Do you want to save changes")
        if message == "yes":
            save()
        else:
            root.destroy()

    def undo():
        text.event_generate("<<Undo>>")

    def cut():
        text.event_generate("<<Cut>>")

    def copy():
        text.event_generate("<<Copy>>")

    def paste():
        text.event_generate("<<Paste>>")

    def delete():
        message = messagebox.askquestion("Notepad", "Do you want to delete all")
        if message == "yes":
            text.delete("1.0", "end")
        else:
            return "break"

    def select_all():
        text.tag_add("sel", "1.0", "end")
        return "break"

    def time():
        d = datetime.now()
        text.insert('end', d)

    def fonts():
        root = tk.Tk()
        root.geometry("400x400")
        root.title("Font")
        l1 = Label(root, text="Font:")
        l1.place(x=10, y=10)
        f = tk.StringVar()
        fonts = ttk.combobox(root, width=15, textvariable=f, state="readonly", font=('verdana', 10, 'bold'), )
        fonts['values'] = font.families()
        fonts.place(x=10, y=10)
        fonts.current(0)
        l2 = Label(root, text="Font Style")
        l2.place(x=180, y=10)
        st = tk.StringVar()
        style = ttk.Combobox(root, width=15, textvariables=st, state="readonly", font=('verdana', 10, "bold"), )
        style["values"] = ("bold", "bold italic", "italic")
        style.place(x=180, y=30)
        style.current(0)

        l3 = Label(root, text="Size")
        l3.place(x=350, y=10)
        sz = tk.StringVar()
        size = ttk.combobox(root, width=2, textvariable=sz, state="readonly", font=("verdana", 10, "bold"), )
        style["values"] = (
        8, 9, 10, 12, 15, 20, 23, 25, 27, 30, 35, 40, 43, 47, 50, 55, 65, 76, 80, 90, 100, 150, 200, 255, 300)
        size.place(x=350, y=30)
        size.current(0)
        sample = LabelFrame(root, text="Sample", height=100, width=200)
        sample["font"] = (fonts.get(), size.get(), style.get())
        sample.place(x=180, y=220)

        l4 = Label(sample, text="This is the sample")
        l4.place(x=20, y=30)

        def OK():
            text["font"] = (fonts.get(), size.get(), style.get())
            root.destroy()

        ok = Button(root, text="OK", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=OK)
        ok.place(x=137, y=350)

        def Apl():
            l4["font"] = (fonts.get(), size.get(), style.get())

        Apply = Button(root, text="Apply", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=Apl)

        def Cnl():
            root.destroy()

        cancel = Button(root, text="Cancel", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=Cnl)

    menubar = Menu(root)

    file = Menu(menubar, tearoff=0)
    file.add_command(label="new", command=new)
    file.add_command(label="new_window", command=new_window)
    file.add_command(label="open", command=open)
    file.add_command(label="save", command=save)
    file.add_separator()
    file.add_command(label="exit", command=exit)
    menubar.add_cascade(label="file", menu=file, font=('verdana', 10, 'bold'))

    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="undo", accelerator="Ctrl+Z", command=undo)
    edit.add_command(label="cut", accelerator="Ctrl+X", command=cut)
    edit.add_command(label="copy", accelerator="Ctrl+C", command=copy)
    edit.add_command(label="paste", accelerator="Ctrl+V", command=paste)
    edit.add_command(label="delete", accelerator="Del", command=delete)
    edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
    edit.add_command(label="Time/Date", accelerator="F5", command=time)
    menubar.add_cascade(label="Edit", menu=edit)

    Format = Menu(menubar, tearoff=0)
    Format.add_command(label="Word Wrap")
    Format.add_command(labal="Font...", command=fonts)
    Format.add_cascade(label="Format", menu=Format)

    Help = Menu(menubar, tearoff=0)
    Help.add_command(label="View Help")
    Help.add_command(label="Send feedback")
    Help.add_command(label="About notepad")
    menubar.add_cascade(label="Help", menu=Help)
    root.config(menu=menubar)

    text = ScrolledText(root, width=1000, height=1000)
    text.place(x=0, y=0)
    root.mainloop()

def open():
    root.filename = filedialog.askopenfilename(initialdir='/', title="select file", filetypes=(("jpeg files",
                                                                                               "*.jpg"),
                                                                                            ("all files", '*.*')))
    file = root.filename
    text.insert('end', file)

def new():
    text.delete("1.0", "end")

def save():
    root.filename = filedialog.asksaveasfile(mode="w", defaultextension=".text")
    if root.filename is None:
        return
    file_save = str(text.get(1.0, END))
    root.filename.write(file_save)
    root.filename.close()

def exit():
    message = messagebox.askquestion("Notepad", "Do you want to save changes")
    if message == "yes":
        save()
    else:
        root.destroy()

def undo():
    text.event_generate("<<Undo>>")

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    message = messagebox.askquestion("Notepad", "Do you want to delete all")
    if message == "yes":
        text.delete("1.0", "end")
    else:
        return "break"

def select_all():
    text.tag_add("sel", "1.0", "end")
    return "break"

def time():
    d = datetime.now()
    text.insert('end', d)

def fonts():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Font")
    l1 = Label(root, text="Font:")
    l1.place(x=10, y=10)
    f = tk.StringVar()
    fonts = ttk.combobox(root, width=15, textvariable=f, state="readonly", font=('verdana', 10, 'bold'),)
    fonts['values'] = font.families()
    fonts.place(x=10, y=10)
    fonts.current(0)
    l2 = Label(root, text="Font Style")
    l2.place(x=180, y=10)
    st= tk.StringVar()
    style = ttk.Combobox(root, width=15, textvariables=st, state="readonly", font=('verdana', 10, "bold"),)
    style["values"] = ("bold", "bold italic", "italic")
    style.place(x=180, y=30)
    style.current(0)

    l3 = Label(root, text="Size")
    l3.place(x=350, y =10)
    sz = tk.StringVar()
    size = ttk.combobox(root, width=2, textvariable=sz, state="readonly", font=("verdana", 10, "bold"),)
    style["values"] = (8,9,10,12,15,20,23,25,27,30,35,40,43,47,50,55,65,76,80,90,100,150,200,255,300)
    size.place(x=350, y=30)
    size.current(0)
    sample = LabelFrame(root, text="Sample", height=100, width=200)
    sample["font"] = (fonts.get(), size.get(), style.get())
    sample.place(x=180, y=220)

    l4 = Label(sample, text="This is the sample")
    l4.place(x=20, y=30)

    def OK():
        text["font"] = (fonts.get(), size.get(), style.get())
        root.destroy()
    ok = Button(root, text="OK", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=OK)
    ok.place(x=137, y=350)

    def Apl():
        l4["font"] = (fonts.get(), size.get(), style.get())

    Apply = Button(root, text="Apply", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=Apl )

    def Cnl():
        root.destroy()

    cancel = Button(root, text="Cancel", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=Cnl)




root = tk.Tk()
root.geometry('500x500')
root.title('Notepad')

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
file.add_command(label="new", command=new)
file.add_command(label="new_window", command=new_window)
file.add_command(label="open", command=open)
file.add_command(label="save", command=save)
file.add_separator()
file.add_command(label="exit", command=exit)
menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))

edit = Menu(menubar, tearoff=0)
edit.add_command(label="undo", accelerator="Ctrl+Z", command=undo)
edit.add_command(label="cut", accelerator="Ctrl+X", command=cut)
edit.add_command(label="copy", accelerator="Ctrl+C", command=copy)
edit.add_command(label="paste", accelerator="Ctrl+V", command=paste)
edit.add_command(label="delete", accelerator="Del", command=delete)
edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
edit.add_command(label="Time/Date", accelerator="F5", command=time)
menubar.add_cascade(label="Edit", menu=edit)

Format = Menu(menubar, tearoff=0)
Format.add_command(label="Word Wrap")
Format.add_command(label="Font...", command=fonts)
menubar.add_cascade(label="Format", menu=Format)

Help = Menu(menubar, tearoff=0)
Help.add_command(label="View Help")
Help.add_command(label="Send feedback")
Help.add_command(label="About notepad")
menubar.add_cascade(label="Help", menu=Help)
root.config(menu=menubar)

text = ScrolledText(root, width=1000, height=1000)
text.place(x=0, y=0)
root.mainloop()
