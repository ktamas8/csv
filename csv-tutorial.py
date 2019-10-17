import pandas as pd
import csv

df = pd.read_csv("hrdata.csv")
#df[['Name','Salary']].head()
print(df['Name'][0])

with open('hrdata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
