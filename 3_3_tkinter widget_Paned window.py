from tkinter import *
tk=Tk()
m1=PanedWindow()
mp=Menubutton(tk,text="gfg")

mp.menu=Menu(mp,tearoff=0)
mp["menu"]=mp.menu
cVar=IntVar()
aVar=IntVar()
mp.menu.add_checkbutton(label="contact",variable=cVar)
mp.menu.add_checkbutton(label="about",variable=aVar)
mp.pack()



m1.pack(fill=BOTH,expand=1)
left=Entry(m1,bd=5)
m1.add(left)

m2=PanedWindow(m1,orient=HORIZONTAL)
m1.add(m2)
top=Scale(m2,orient=HORIZONTAL)
m2.add(top)

mainloop()
