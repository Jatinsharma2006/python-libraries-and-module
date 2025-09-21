from tkinter import *
win=Tk()

Photo_img=PhotoImage(file="E:/python projects/30-40 Tkinter/id card project all parts/abc.png")


lbl=Label(win,image=Photo_img)
lbl.pack(expand=YES)


btn=Button(win,image=Photo_img)
btn.pack(expand=YES)


win.mainloop()






