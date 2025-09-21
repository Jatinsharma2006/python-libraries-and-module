from tkinter import *
from tkinter import messagebox


def open_dialog():
    top=Toplevel(win)
    top.title("TOP LEVEL DIALOG")

    Label(top,text="This is a TOP LEVEL DIALOG").pack(pady=20)
    Button(top,text="CLOSE",command=top.destroy).pack(pady=10)


win=Tk()
win.title("Main Window")
win.geometry('400x1200')  

Button(win,text="OPEN DIALOG",command=open_dialog).pack(pady=20)


win.mainloop()
