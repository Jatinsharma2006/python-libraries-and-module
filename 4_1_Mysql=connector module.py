#installing mysql-drivers as: pip install mysql-connector-python
import mysql.connector as my

con=my.connect(user='root',database='resume',password='apexs7777')

cursor=con.cursor() #Cursor is temporary  memory buffer to store data
query='select name,english from candidates'

cursor.execute(query)#execute the query

#Display data using for loop
for(name,english)in cursor:
    print(name,english)


#Close resources
cursor.close()
con.close()
