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




import numpy as np


acc_data = np.random.randint(-10, 10, 10) 
acc_time = np.arange(10)



acc = Accelerometer(
    name="Accelerometer",
    location="haldia",
    record_date="2023-01-09"

)

acc.add_data(
    data = acc_data,
    time = acc_time 
)

print(" Accelerometer Data ",acc.data)