from OriginalKalmanAngle.Kalman import KalmanAngle
import time
import math
import csv
from pandas import *

kalmanX = KalmanAngle()
kalmanY = KalmanAngle()

# countless initialisation
# creating empty lists
accelDataX = []
accelDataY = []
accelDataZ = []
gyroDataX = []
gyroDataY = []
gyroDataZ = []
magDataX = []
magDataY = []
magDataZ = []
accX = 0
accY = 0
accZ = 0
gyroX = 0
gyroY = 0
gyroZ = 0
magX = 0
magY = 0
magZ = 0

RestrictPitch = False	#Comment out to restrict roll to ±90deg instead - please read: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf
radToDeg = 57.2957786
kalAngleX = 0
kalAngleY = 0
header = []


# open the file in read mode
file = open('./csvs/14anov.csv', 'r')

# creating dictreader object
file = csv.DictReader(file)
print(file)

# iterating over each row and append
# values to empty list
for col in file:
	if (col['accelX'] != None and col['accelY']!=None and col['accelZ']!=None and col['gyroX']!=None and col['gyroY']!=None and col['gyroZ']!=None and col['magnoX']!=None and col['magnoY']!=None and col['magnoZ']!=None):
		accelDataX.append(float(col['accelX']))
		accelDataY.append(float(col['accelY']))
		accelDataZ.append(float(col['accelZ']))
		gyroDataX.append(float(col['gyroX']))
		gyroDataY.append(float(col['gyroY']))
		gyroDataZ.append(float(col['gyroZ']))
		magDataX.append(float(col['magnoX']))
		magDataY.append(float(col['magnoY']))
		magDataZ.append(float(col['magnoZ']))

accX = accelDataX[0]
accY = accelDataY[0]
accZ = accelDataZ[0]

# loading data is complete!

if (RestrictPitch):
	roll = math.atan2(accY,accZ) * radToDeg
	pitch = math.atan(-accX/math.sqrt((accY**2)+(accZ**2))) * radToDeg

else:
	roll = math.atan(accY/math.sqrt((accX**2)+(accZ**2))) * radToDeg
	pitch = math.atan2(-accX,accZ) * radToDeg
	
kalmanX.setAngle(roll)
kalmanY.setAngle(pitch)
gyroXAngle = roll;
gyroYAngle = pitch;
compAngleX = roll;
compAngleY = pitch;


timer = time.time()
flag = 0
index = 0
while True:
	#Read raw values one after another
	index += 1
	accX = accelDataX[index]
	accY = accelDataY[index]
	accZ = accelDataZ[index]

	gyroX = gyroDataX[index]
	gyroY = gyroDataY[index]
	gyroZ = gyroDataZ[index]

	magX = magDataX[index]
	magY = magDataY[index]
	magZ = magDataZ[index]

	dt = time.time() - timer
	timer = time.time()

	if (RestrictPitch):
		roll = math.atan2(accY,accZ) * radToDeg
		pitch = math.atan(-accX/math.sqrt((accY**2)+(accZ**2))) * radToDeg
	else:
		roll = math.atan(accY/math.sqrt((accX**2)+(accZ**2))) * radToDeg
		pitch = math.atan2(-accX,accZ) * radToDeg	

	gyroXRate = gyroX/131
	gyroYRate = gyroY/131

	if (RestrictPitch):

		if((roll < -90 and kalAngleX >90) or (roll > 90 and kalAngleX < -90)):
			kalmanX.setAngle(roll)
			complAngleX = roll
			kalAngleX   = roll
			gyroXAngle  = roll
		else:
			kalAngleX = kalmanX.getAngle(roll,gyroXRate,dt)

		if(abs(kalAngleX)>90):
			gyroYRate  = -gyroYRate
			kalAngleY  = kalmanY.getAngle(pitch,gyroYRate,dt)
	else:

		if((pitch < -90 and kalAngleY >90) or (pitch > 90 and kalAngleY < -90)):
			kalmanY.setAngle(pitch)
			complAngleY = pitch
			kalAngleY   = pitch
			gyroYAngle  = pitch
		else:
			kalAngleY = kalmanY.getAngle(pitch,gyroYRate,dt)

		#if(abs(kalAngleY)>90):
		gyroXRate  = -gyroXRate
		kalAngleX = kalmanX.getAngle(roll,gyroXRate,dt)

	#angle = (rate of change of angle) * change in time
	gyroXAngle = gyroXRate * dt
	gyroYAngle = gyroYAngle * dt

	#compAngle = constant * (old_compAngle + angle_obtained_from_gyro) + constant * angle_obtained from accelerometer
	compAngleX = 0.93 * (compAngleX + gyroXRate * dt) + 0.07 * roll
	compAngleY = 0.93 * (compAngleY + gyroYRate * dt) + 0.07 * pitch

	if ((gyroXAngle < -180) or (gyroXAngle > 180)):
		gyroXAngle = kalAngleX
	if ((gyroYAngle < -180) or (gyroYAngle > 180)):
		gyroYAngle = kalAngleY

	print("Angle X: " + str(kalAngleX)+"   " +"Angle Y: " + str(kalAngleY))
	#print(str(roll)+"  "+str(gyroXAngle)+"  "+str(compAngleX)+"  "+str(kalAngleX)+"  "+str(pitch)+"  "+str(gyroYAngle)+"  "+str(compAngleY)+"  "+str(kalAngleY))
	time.sleep(0.005)
