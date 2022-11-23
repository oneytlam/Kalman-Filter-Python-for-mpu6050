# importing the module
import csv 
# open the file in read mode
file = open('./csvs/x1.csv', 'r')

# creating dictreader object
file = csv.DictReader(file)
print(file)

# creating empty lists
accelX = []
accelY = []
accelZ = []
 
# iterating over each row and append
# values to empty list
for col in file:
    accelX.append(col['accelX'])
    accelY.append(col['accelY'])
    accelZ.append(col['accelZ'])
    
print(float(bool(None)))