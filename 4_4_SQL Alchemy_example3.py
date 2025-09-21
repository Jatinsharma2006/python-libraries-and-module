#Converting Pandas Table to Html

from sqlalchemy import create_engine
import pandas as pd

db = create_engine("mysql+pymysql://root:apexs7777@localhost/mydb")
con=db.connect()

sql="SELECT * FROM friend limit 0,10"
df = pd.read_sql(sql, con)

pd.options.display.float_format ='{:.0f}'.format

html = df.to_html()
con.close()
db.dispose()

f=open("output.html", "w")
f.write(html)
f.close()

import webbrowser, os
webbrowser.open(f"file://{os.path.abspath('output.html')}")
