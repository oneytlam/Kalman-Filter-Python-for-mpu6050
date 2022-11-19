import time
import math
import csv
from pandas import *

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

# open the file in read mode
file = open('./csvs/14anov.csv', 'r')
# creating dictreader object
file = csv.DictReader(file)

for col in file:
	if (col['accelX'] != None and col['accelY']!=None and col['accelZ']!=None and col['gyroX']!=None and col['gyroY']!=None and col['gyroZ']!=None):
		accelDataX.append(float(col['accelX']))
		accelDataY.append(float(col['accelY']))
		accelDataZ.append(float(col['accelZ']))
		gyroDataX.append(float(col['gyroX']))
		gyroDataY.append(float(col['gyroY']))
		gyroDataZ.append(float(col['gyroZ']))

accX = accelDataX[0]
accY = accelDataY[0]
accZ = accelDataZ[0]

print(accelDataX)