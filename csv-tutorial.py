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

post_data="{ "identifier": "floor-lamp6", "name": "Floor Lamp6", "device_type": "switch", "controller_gateway": "192.168.0.6" }"

url_request.get_url("http://localhost:5000/device/floor-lamp")
url_request.post_url("http://localhost:5000/devices", post_data)

#x = Person("John", "Doe")
#x.printname()
#x = Student("Mike", "Olsen",2019)
#x.welcome()
