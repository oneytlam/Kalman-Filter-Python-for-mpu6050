from pandas import *
data = read_csv("./csvs/x1.csv")
accelX = data['accelX'].tolist()
accelY = data['accelY'].tolist()
accelZ = data['accelZ'].tolist()
gyroX = data['accelX'].tolist()
gyroY = data['accelY'].tolist()
gyroZ = data['accelZ'].tolist()
print(accelX)