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

# open the file in read mode
file = open('./csvs/manysensors.csv', 'r')
# creating dictreader object
file = csv.DictReader(file)

for col in file:
	timeStamp.append(col["timestamp"])
	if (col['gravityX'] != None and col['gravityY'] != None and col['gravityZ'] != None):
		if (col['accelX'] != None and col['accelY'] != None and col['accelZ']!=None and col['gyroX']!=None and col['gyroY']!=None and col['gyroZ']!=None):
			accelDataX.append(float(col['accelX']) - float(col['gravityX']))
			accelDataY.append(float(col['accelY']) - float(col['gravityY']))
			accelDataZ.append(float(col['accelZ']) - float(col['gravityZ']))
			gyroDataX.append(float(col['gyroX']))
			gyroDataY.append(float(col['gyroY']))
			gyroDataZ.append(float(col['gyroZ']))
		#Assuming that if data is recorded, x, y and z values are present
		if (col['accelX'] == None and col['gyroX'] == None):
			accelDataX.append(float(col['accelX']) - float(col['gravityX']))
			accelDataY.append(float(col['accelY']) - float(col['gravityY']))
			accelDataZ.append(float(col['accelZ']) - float(col['gravityZ']))
			gyroDataX.append(float(0))
			gyroDataY.append(float(0))
			gyroDataZ.append(float(0))
		if (col['accelX'] != None and col['gyroX'] == None):
			accelDataX.append(float(col['accelX']) - float(col['gravityX']))
			accelDataY.append(float(col['accelY']) - float(col['gravityY']))
			accelDataZ.append(float(col['accelZ']) - float(col['gravityZ']))
			gyroDataX.append(float(0))
			gyroDataY.append(float(0))
			gyroDataZ.append(float(0))
		if (col['accelX'] == None and col['gyroX'] != None):
			accelDataX.append(float(0))
			accelDataY.append(float(0))
			accelDataZ.append(float(0))
			gyroDataX.append(float(col['gyroX']))
			gyroDataY.append(float(col['gyroY']))
			gyroDataZ.append(float(col['gyroZ']))

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
    print(f"time: {curTime}, x coordinate: {x_coordinate}, y coordinate: {y_coordinate}")