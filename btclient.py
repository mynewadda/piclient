from  bluetooth import *
def data():
     from sense_hat import SenseHat
     sense=SenseHat()
     sense.clear()
     pressure=sense.get_pressure()
     sense.clear()
     temp=sense.get_temperature()
     sense.clear()
     humidity=sense.get_humidity()
     sense.clear()
  #   o=sense.get_orientation()
   #  pitch=o["pitch"]
    # yaw=o["yaw"]
     #roll=o["roll"]
     sense.clear()
    
     data={"pressure":pressure,"temperature":temp,"humidity":humidity}

      
     return(str(data))


servermac='D4:6D:6D:FD:F8:03'
port=30
s=BluetoothSocket( RFCOMM )
s.connect((servermac,port))
while 1:
    data1=data()
    s.send(data1)
    if data1=="quit":
         break

s.close()
