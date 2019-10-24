import pandas as pd
import csv
import url_request

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

post_data="{ "identifier": "floor-lamp4", "name": "Floor Lamp5", "device_type": "switch", "controller_gateway": "192.168.0.5" }"

url_request.get_url("http://localhost:5000/device/floor-lamp")
url_request.put_url("http://localhost:5000/device/floor-lamp", post_data)

#x = Person("John", "Doe")
#x.printname()
#x = Student("Mike", "Olsen",2019)
#x.welcome()
