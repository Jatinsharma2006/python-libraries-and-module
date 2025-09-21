from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=Tk()
win.title("Combbox")

city=StringVar(value= "")
#write event handling code as per need
def cityChanged(event):
    a=event.widget.get()
    messagebox.showinfo('Result',f'You have selected :  {city.get()}')

#Designing UI
L1=Label(win,text="SELECT YOUR CITY OF RESIDENCE")
L1.pack()
                       
C1=ttk.Combobox(win,width=30,textvariable=city)
C1['values']=('Bhopal','Ujjain','Indore')
C1.current(2) #tell what to select as defalt value
C1.bind("<<ComboboxSelected>>",cityChanged)
C1.pack()

win.mainloop()

print(city)
