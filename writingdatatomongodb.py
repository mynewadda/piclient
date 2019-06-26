# Python code to illustrate 
# inserting data in MongoDB 

from pymongo import MongoClient 
client = MongoClient("mongodb://Kumar:galaxymilk3%23@cluster1-shard-00-00-jz1pv.mongodb.net:27017,cluster1-shard-00-01-jz1pv.mongodb.net:27017,cluster1-shard-00-02-jz1pv.mongodb.net:27017/measurements?ssl=true&replicaSet=Cluster1-shard-0&authSource=admin&w=majority")
db = client.measurements

import bluetooth
hostMACAddress = 'D4:6D:6D:FD:F8:03'
port = 30
backlog = 1
size = 1024

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# database 
db=client.measurements

# Created or Switched to collection names 
collection = db.measurements

s.bind((hostMACAddress, port))
s.listen(backlog)
client, clientInfo = s.accept()
print ("accepted client")
while 1:
   data = str(client.recv(size))
  
   data=data.partition('b')
   data=data[2]
   data=data.partition('{')
   data=data[2]
   data=data.partition('}')
   data=data[0]
   Dict = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in data.split(', ')))
   data1=Dict
   
  
   humidity=float(data1["'humidity'"])
   temperature=float(data1["'temperature'"])
   pressure=float(data1[("'pressure'")])
   emp_rec1 = { 
        "temp":temperature,
        "pressure":pressure,
        "humidity":humidity
        } 
   rec_id1 = collection.insert_one(emp_rec1) 
   print("Data inserted with record ids",rec_id1)


