                     #WORKING  WITH .CSV FILE

#METHOD I: USING csv Module

import csv
#"Writing to a  csv file"
data=[["Name","Age","City"],["Rancho","18","Bhopal"],["Farhan","19","Indore"]]

with open("output.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows(data)

#Reading from a CSV file
with open("output.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)



#METHOD II: USING Pandas Module

import pandas as pd
df=pd.DataFrame(data)
df.to_csv("output2.csv",index=False)

#Reading from a CSV file
df=pd.read_csv("output2.csv")
print(df)





















