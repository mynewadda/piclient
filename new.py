import requests
import random
import datetime
import json
import re
headers = {
    'Accept': 'application/vnd.com.nsn.cumulocity.measurement+json; charset=UTF-8; ver=0.9',
    'Content-type': 'application/vnd.com.nsn.cumulocity.measurement+json; charset=UTF-8; ver=0.9',
}
import bluetooth
hostMACAddress = 'D4:6D:6D:FD:F8:03'
port = 30
backlog = 1
size = 1024

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)



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
   now=datetime.datetime.now()
   d1=str(now.isoformat())
   d1=d1.partition('.')[0]
   d1=str(d1)+".123+02:00"
   
   
  
   data_temp={ "c8y_TemperatureMeasurement": {"T": { "value":temperature,"unit":"C"}},"time":d1,"source": {"id": "31000"},"type":"c8y_PTCMeasurement"}
   response_temp = requests.post('http://raspberrypidata.eu-latest.cumulocity.com/measurement/measurements/', headers=headers, data=json.dumps(data_temp), auth=('thankunisha@gmail.com', 'galaxymilk3'))
   
  
   data_humidity={ "c8y_HumidityMeasurement": {"T": { "value":humidity,"unit":"%"}},"time":d1,"source": {"id": "31000"},"type":"c8y_PTCMeasurement"}
   response_humidity = requests.post('http://raspberrypidata.eu-latest.cumulocity.com/measurement/measurements/', headers=headers, data=json.dumps(data_humidity), auth=('thankunisha@gmail.com', 'galaxymilk3'))

   
  
   data_pressure={ "c8y_Pressure Measurement": {"T": { "value":pressure,"unit":"mbar"}},"time":d1,"source": {"id": "31000"},"type":"c8y_PTCMeasurement"}
   response_pressure = requests.post('http://raspberrypidata.eu-latest.cumulocity.com/measurement/measurements/', headers=headers, data=json.dumps(data_pressure), auth=('thankunisha@gmail.com', 'galaxymilk3'))

   rdict={'pressure':response_pressure,'humidity':response_humidity,'temperature':response_temp}
   print(rdict)    
    
client.close()
s.close()

