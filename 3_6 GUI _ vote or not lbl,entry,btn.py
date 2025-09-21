from tkinter import *
from tkinter import messagebox


win=Tk()
win.title("Vote of Not")
win.geometry('400x1200')
win.config(bg='orange')
age=IntVar(value=18)  # default value
def voteClick():
    a=age.get()    #get value of Entry into a
    if a>=18:
        messagebox.showinfo('YOU ARE ELIGABLE','YOU CAN  VOTE')
    else:
        messagebox.showwarning("Sorry","YOU CAN'T VOTE")




lblAge=Label(win,text="Enter Your Age",font=("bell MT",30))
txtAge=Entry(win,width=10,font=("bell MT",30),textvariable=age)
btnVote=Button(win,text="Show Result",font=("bell MT",15),command=voteClick)


lblAge.pack(side="top",padx=10,pady=10)
txtAge.pack(side="top",ipadx=10,padx=10,pady=15)
btnVote.pack(side="top",ipadx=10,padx=10,pady=15)



win.mainloop()



