import serial
import time

arduino = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2) # waiting the initialization...
print("initialising")

arduino.write('I') # init
# time.sleep(2) 
# arduino.write('B') 
# time.sleep(2) 
# arduino.write('C') 
# time.sleep(2) 
# arduino.write('D')
# time.sleep(2)
# arduino.write('E') 
# time.sleep(2)
# arduino.write('F') 


# while 1:
#     sensorValue = arduino.readline()
#     print(sensorValue)

arduino.close() #say goodbye to Arduino
