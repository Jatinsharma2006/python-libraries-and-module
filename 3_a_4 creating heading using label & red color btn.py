#using tkinter label 
from tkinter import*
win=Tk()
win.geometry('600x600')
win.title('hello')
lblMsg=Label(win,text="-------Arduino Python Integreation------"\
            ,fg="white",bg="green",font=("bell MT",30))#fg="white" calls initializers fn
lblMsg.pack()



#using tkinter label=lbl  and button=btn


def redClick():         #what happes when we click redbutton
    pass                #do noting

btnRed=Button(win,text="red",height=3,width=5,bg="red", command=redClick)
btnRed.pack(pady=30)
win.mainloop()










