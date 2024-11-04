import serial

ser = serial.Serial("COM5", baudrate=9600, timeout=1)
while True:
   data = ser.readline()
   print(data)
   