#Using Sql Alchemy Framework to connect with database
#pip install sqlalchemy pymysql pandas


from sqlalchemy import create_engine
import pandas as pd

"STEP I:Obtain connection"
engine = create_engine("mysql+pymysql://root:apexs7777@localhost/resume")

"STEP II:Design sql query and pass it to read_sql fn of pandas"
sql="SELECT * FROM candidates"


"Step III:Pass Query,engine to it"
df = pd.read_sql(sql,engine)


"STEP IV:Display dataframe"
print(df)
