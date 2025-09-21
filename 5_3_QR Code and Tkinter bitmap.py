import pyqrcode 
import tkinter

#xbm(scale=1, quiet_zone=4)

code = pyqrcode.create('Knights who say ni!')
code_xbm = code.xbm(scale=5)

top = tkinter.Tk()
code_bmp = tkinter.BitmapImage(data=code_xbm)
code_bmp.config(foreground="black")
code_bmp.config(background="white")
label = tkinter.Label(image=code_bmp)
label.pack()

