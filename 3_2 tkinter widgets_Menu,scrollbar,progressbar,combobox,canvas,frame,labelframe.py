from tkinter import *
from tkinter import ttk
win=Tk()

#win.geometry('600x600')
menubar=Menu(win)
file=Menu(menubar,tearoff=1)
help=Menu(menubar,tearoff=0)
file.add_command(label="NEW",command=lambda:menuClick("NEW"))

file.add_command(label="OPEN",command=lambda:menuClick("OPEN"))
help.add_command(label="ABOUT US",command=lambda:menuClick("ABOUT US"))
help.add_separator()
help.add_command(label="EXIT",command=win.destroy)
menubar.add_cascade(label="Hello",menu=file)
menubar.add_cascade(label="Help",menu=help)
win.config(menu=menubar)


#scrollbar
scrollbar=Scrollbar(win,orient=HORIZONTAL)
scrollbar.pack()
mylist=Listbox(win,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,'this is line number'+str(line))
mylist.pack()
scrollbar.config(command=mylist.yview)


#progressbar
import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.1)
        progress['value']=i
        win.update_idletasks()
    progress.stop()

win.title("progressbar example")
progress=ttk.Progressbar(win,length=300,mode="determinate")
progress.pack(pady=50)
  
start=Button(win,text="start",command=start_progress)
start.pack()


#combobox
def hello():
    ok=cmbox.get()
    print(ok)
     

win.title("COMBOBOX EXAMPLE")

VALUE=["OPTION1","OPTION2","OPTION3","OPTION4"]
cmbox=ttk.Combobox(win,value=VALUE)
cmbox.pack()
cmbox.set("hello")
btn=Button(win,text="start",command=hello)
btn.pack()




#canvas
h=Canvas(win,width=500,height=600,bg="black")
h.pack()
Canvas_height=200
Canvas_width=200
h.create_line(150,120,350,50,fill="green")
h.create_arc(150,120,350,210,start=0,extent=220,fill="red")

#frame
left=Label(one,text="INSIDE THE LABEL")
left.pack(expand=YES,fill=BOTH)
two=Frame(one,bg="blue",bd=5)
two.pack(expand=YES,fill=BOTH)

left=Label(two,text="INSIDE THE LABEL")
left.pack(expand=YES,fill=BOTH)
one.pack(expand=YES,fill=BOTH)

#label frame
left=LabelFrame(tk,text="INSIDE THE LABELFRAME",bg="yellow",bd=5)
left.pack(expand=YES,fill=BOTH)
mainloop()




