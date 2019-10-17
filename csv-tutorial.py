import pandas as pd
import csv
import url-request

df = pd.read_csv("hrdata.csv")
#df[['Name','Salary']].head()
print(df['Name'][0])

with open('hrdata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:

        dates = []

        name = row[0]
        date = row[1]
        salary = row[2]
        sick = row[3]

        dates.append(date)
        print(name + " " + salary)

url-request.get_url("127.0.0.1")

#x = Person("John", "Doe")
#x.printname()
#x = Student("Mike", "Olsen",2019)
#x.welcome()
