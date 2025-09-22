from tkinter import *
from tkcalendar import Calendar

def display_date():
    selected_date= calendar.get_date()
    result_label.config(text=f'Selected Date:{selected_date}')


win=Tk()
win.title("TechDev Calendar Example")
win.geometry('600x400')  


calendar=Calendar(win,selectmode="day")
calendar.pack(pady=20)

Button(win,text="Get Date",command=display_date).pack()

result_label=Label(win,text="No Date Selected")
result_label.pack()

win.mainloop()
