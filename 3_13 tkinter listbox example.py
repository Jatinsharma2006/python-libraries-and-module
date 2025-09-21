from tkinter import *



def show_selection():
    selected_item=lb.get(lb.curselection())
    result_label.config(text=f'Selected:{selected_item}')


win=Tk()
win.title("Listbox Example")
win.geometry('600x400')  


lb=Listbox(win)
lb.insert(1,'PYTHON')
lb.insert(3,'C')
lb.insert(4,'C++')
lb.insert(5,'JAVA')
lb.insert(5,'JAVA SCRIPT')
lb.pack(pady=20)

Button(win,text="Show Selection",command=show_selection).pack()

result_label=Label(win,text="No Item selected")
result_label.pack()

win.mainloop()
