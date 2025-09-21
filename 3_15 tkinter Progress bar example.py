#Advance concept:Using progressbar

from tkinter import *
from tkinter import ttk

def start_progress():
    progress_bar.start(10)
    
def stop_progress():
    progress_bar.stop()

    
win = Tk()
win.geometry('600x400')
win.title("Progress Bar Example")


progress_bar=ttk.Progressbar(win,orient="horizontal",length=300,mode="indeterminate")
progress_bar.pack(pady=20)


Button(win,text="START", command=start_progress).pack(side="left",padx=20)
Button(win,text="STOP", command=stop_progress).pack(side="right",padx=20)
 

win.mainloop()
