# importing the module
import csv 
# open the file in read mode
filename = open('./csvs/x1.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
accelX = []
totalprofit = []
totalunit = []
 
# iterating over each row and append
# values to empty list
for col in file:
    accelX.append(col['accelX'])
    totalprofit.append(col['moisturizer'])
    totalunit.append(col['total_units'])

accelX = []
accelX = data['accelX'].tolist()
accelY = data['accelY'].tolist()
accelZ = data['accelZ'].tolist()
gyroX = data['accelX'].tolist()
gyroY = data['accelY'].tolist()
gyroZ = data['accelZ'].tolist()
print(accelX)