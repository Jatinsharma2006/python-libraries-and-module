from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("MENU")
win.geometry('400x1200')
win.config(bg='grey')

def menuClick(text):
      messagebox.showinfo('search',f"you have selected{text}")

menubar=Menu(win)
file=Menu(menubar,tearoff=0)
help=Menu(menubar,tearoff=1)


file.add_command(label="new",command=lambda:menuClick('New'))
file.add_command(label="open",command=lambda:menuClick('Open'))
file.add_command(label="save as",command=lambda:menuClick('Save As'))
file.add_command(label="ok",command=lambda:menuClick('OK'))


help.add_command(label="about us",command=lambda:menuClick('About us'))
help.add_command(label="new",command=lambda:menuClick('New'))
help.add_command(label="new",command=lambda:menuClick('New'))


help.add_separator()
help.add_command(label="Exit",command=win.destroy)

menubar.add_cascade(label='File',menu=file)
menubar.add_cascade(label='Help',menu=help)
win.config(menu=menubar)
