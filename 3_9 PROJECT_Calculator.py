from tkinter import *

def draw(buttonName,side): 
    obj=Frame(buttonName,borderwidth=4,bd=4,bg="lime")
    obj.pack(side=side,expand=YES,fill=BOTH)
    return obj

def button(buttonName,side,text,command=None):
    obj=Button(buttonName,text=text,command=command)
    obj.pack(side=side,expand=YES,fill=BOTH)
    return obj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title("lets calulate")
        self.display=StringVar()
        Entry(self,relief=RIDGE,textvariable=self.display,justify="right",bd=30,bg="lime")\
                        .pack(side=TOP,expand=YES,fill=BOTH)
        for clearButton in(["C"]):
            erase=draw(self,TOP)
            for i in clearButton:
                button(erase,LEFT,i,command=self.clearClick)
                
        for numButton in("789/","456*","123-","0.+"):
            FunctionNum=draw(self,TOP)
            for btn in numButton:
                button(FunctionNum,LEFT,btn,lambda
                    obj=self.display,q=btn:obj.set
                    (obj.get()+q))



        EqualButton=draw(self,TOP)
        for btn in"=":
            
            if btn=="=":
                btniEquals=button(EqualButton,LEFT,btn)
                btniEquals.bind('<ButtonRelease-1>',lambda e,s=self,
                                obj=self.display:s.calculate(obj),"+")
            else:
                btniEquals=button(EqualButton,LEFT,btn,
                    lambda obj=self.display,s='%s'%btniEquals:obj.set(obj.get()+s))
    def calculate(self,display):
        try:
            self.display.set(eval(self.display.get()))
        except:
            display.set("ERROR")
    def clearClick(self):
            self.display.set("")
if __name__=='__main__':
    app().mainloop()
                    







                    
                    
    
