from my_sensor import Accelerometer,Gyro, GPS
import numpy as np

acc = Accelerometer(
    name="Accelerometer",
    loaction="Haldia",
    record_date="2023-02-10"
)

gyro= Gyro(
    name="Gyroscope",
    location="kolkata",
    record_date="2023-01-10"

)

gps =GPS(
    name="GPS",
    location="Mumbai"
    record_date="2023-01-10"
    brand="espressif"
)
#Get all the dummy data
time = np.arange(10)
acc_data = np.random.randint(-10,10,10)
gyro_data = np.random.randint(-15,15,10)
gps_data = np.random.randint(-12,12,10)


#add data to the instance
print(acc.name)
print(acc.location)
print(acc.recod_date)

acc.add_data(
    data=acc_data,
    time=time
)
print(gyro.name)
print(gyro.location)
print(gyro.record_date)
gyro.add_data(
    data=gps_data,
    time=time
)

print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
