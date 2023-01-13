class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data={}
        


    def add_data(self, data, time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully")

    def clear_data(self):
        self.data={}
        print("Data removed successfully")

import numpy as np   


sensor1 = Sensor(name="sensor1",
                 location="haldia",
                 record_date="2023-01-09"
                  )

data = np.random.randint(-10, 10, 10) 
time = np.arange(10)

sensor1.add_data(
    data=data, 
    time=time
                )
print("Genric Sensor data ",sensor1.data)  


class Accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")

acc = Accelerometer(
    name="Accelerometer",
    location="haldia",
    record_date="2023-01-09"

)



import numpy as np


acc_data = np.random.randint(-10, 10, 10) 
acc_time = np.arange(10)

class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")



gyro_data= np.random.randint(-15,15,10)
gyro_time= np.arange(10)

gyro= Gyro(
                  name="Gyroscope",
                  loaction="Haldia",
                  record_date="2023-01-10"
)

gyro.add_data(time=gyro_time,data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()



# GPS attributes:
# name loaction
# record_date
# brand
class GPS(Sensor):
    def __init__(self,name, location,record_date,brand):
        super().__init__(
            name, location, record_date
        )
        self.brand= brand

gps= GPS(
    name="GPS",
    loaction="chennai",
    record_date="2023-01-10",
    brand="espressi"

)

print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)








