import time
import math
import csv
from pandas import *

timeStamp = []
accelDataX = []
accelDataY = []
accelDataZ = []
gyroDataX = []
gyroDataY = []
gyroDataZ = []
accX = 0
accY = 0
accZ = 0
gyroX = 0
gyroY = 0
gyroZ = 0
angleX = 0
angleY = 0
angleZ = 0
velocityX = 0
velocityY = 0
velocityZ = 0
x_coordinate = 0
y_coordinate = 0
z_coordinate = 0
THRESHOLD = 1

# open the file in read mode
file = open('./csvs/manysensors.csv', 'r')
# creating dictreader object
file = csv.DictReader(file)

for col in file:
    startTime = float(col['timestamp'])
    break

def check(val, threshold):
    if abs(val) < threshold:
        return 0
    return val

for col in file:
    timeStamp.append(float(col["timestamp"]) - startTime)
    accelX = float(col['laccX']) if col['laccX'] != None else 0
    accelDataX.append(check(accelX, THRESHOLD))
    
    accelY = float(col['laccY']) if col['laccY'] != None else 0
    accelDataY.append(check(accelY, THRESHOLD))
    
    accelZ = float(col['laccZ']) if col['laccZ'] != None else 0
    accelDataZ.append(check(accelZ, THRESHOLD))
    
    gyroDataX.append(float(col['gyroX']) if col['gyroX'] != None else 0)
    gyroDataY.append(float(col['gyroY']) if col['gyroY'] != None else 0)
    gyroDataZ.append(float(col['gyroZ']) if col['gyroZ'] != None else 0)
		

prevTime = math.floor(float(timeStamp[0]))
curTime = 0

for i in range(len(accelDataX)):
    angleX += gyroDataX[i]
    angleX %= (2*math.pi)
    angleY += gyroDataY[i]
    angleY %= (2*math.pi)
    accX = accelDataX[i] * math.cos(angleX) + accelDataX[i] * math.sin(angleY)
    accY = accelDataY[i] * math.sin(angleX) + accelDataY[i] * math.cos(angleY)
    #assume uniform acceleration
    curTime = float(timeStamp[i])
    x_coordinate += velocityX * (curTime - prevTime) + 0.5 * accX * ((curTime - prevTime) ** 2)
    y_coordinate += velocityY * (curTime - prevTime) + 0.5 * accY * ((curTime - prevTime) ** 2)
    velocityX += accX * (curTime - prevTime)
    velocityY += accY * (curTime - prevTime)
    prevTime = curTime
    print(f"time: {curTime} x coordinate: {x_coordinate}, y coordinate: {y_coordinate}")
