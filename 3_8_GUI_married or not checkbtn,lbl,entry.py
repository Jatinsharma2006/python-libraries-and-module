from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("check box")
win.geometry('400x1200')
win.config(bg='cyan')


name=StringVar()
married=StringVar(value='T')



def resultClick():
    status=married.get()
    n=name.get()
    if status=="N":
        msg=f"hello{n},you are Happy"
        messagebox.showinfo("Result",msg)
    else:
        msg=f"Sorry  {n}  ,you are Sad"
        messagebox.showwarning ("Result",msg)



l1=Label(win,text="Enter Name",font=("bell MT",30))
t1=Entry(win,width=40,textvariable=name,font=("bell MT",30))
c1=Checkbutton(win,text="ARE YOU MARRIED?",font=("bell MT",30),variable=married,onvalue="Y",offvalue="N",command=resultClick)


l1.pack(side="top",ipadx=10,padx=10,pady=15)
t1.pack(side="top",ipadx=10,padx=10,pady=15)
c1.pack(side="top",ipadx=10,padx=10,pady=15)



win.mainloop()
