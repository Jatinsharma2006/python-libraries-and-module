#Converting Pandas Table to Html
#pip install pandastable
import pandas as pd
from tkinter import *
from sqlalchemy import create_engine
from pandastable import Table,TableModel


win=Tk()
win.title("Mysql Table")
win.geometry('800x600')

frame=Frame(win)
frame.pack(fill=BOTH,expand=True)

db = create_engine("mysql+pymysql://root:apexs7777@localhost/resume")
con=db.connect()

sql="SELECT * FROM candidates limit 0,10"
df = pd.read_sql(sql, con)

#Display Pandas Table
table=Table(frame,dataframe=df,showtoolbar=True,showstatusbar=True)
table.show()

con.close()
db.dispose()

win.mainloop()


















