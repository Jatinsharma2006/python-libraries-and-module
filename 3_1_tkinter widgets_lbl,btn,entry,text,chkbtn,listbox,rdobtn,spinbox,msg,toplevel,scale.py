from tkinter import *
win=Tk()
win.geometry('600x600')

#label
w=Label(win,text="hello")
w.pack()

#button
a=Button(win,text="stop",width=4,command=win.destroy)
a.pack()

#entry
b=Entry(win,textvariable=w,width=4)
b.pack()

#text
t=Text(win,height=4,width=4)
t.pack()
t.insert(END,'Greeks of Geeks\nBEST WEBSITE\n')

#checkbutton
married=BooleanVar(value=True)
c=Checkbutton(win,text="married or not",variable=married,offvalue=False,onvalue=True)
c.pack()

#listbox
lb=Listbox(win)
lb.insert(1,'PYTHON')
lb.insert(3,'C')
lb.insert(4,'C++')
lb.insert(5,'JAVA')
lb.pack()

#radio button
gender=StringVar(value="m")
Label(win,text="SELECT GENDER".upper()).pack()

rdoMale=Radiobutton(win,value="m",text="Male",variable=gender)

rdoFemale=Radiobutton(win,value="f",text="Female",variable=gender)
rdoFemale.pack()
rdoMale.select()
rdoMale.pack()

#spinbox
age=IntVar(value=18)
Label(win,text="Enter age").pack()
spiAge=Spinbox(win,textvariable=age,from_=5,to=100)
spiAge.pack()

#message
ourmessage="this is our message"
MessageVar=Message(win,text=ourmessage)
MessageVar.config(bg="lightgreen")
MessageVar.pack()

#scale
r=Scale(win,from_=0,to=42)
r.pack()
l=Scale(win,from_=0,to=200,orient=HORIZONTAL)
l.pack()


#top level
top=Toplevel()
top.title('python')
top.mainloop()

win.mainloop()
