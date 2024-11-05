import serial
from DegreeConverter import DegreeConverter

def convertToDeg(resistance: int) -> int:
   return 180 - int((resistance - 0) * (180 - 0) / (255 - 0) + 0)

ser = serial.Serial("COM4", baudrate=9600, timeout=1)
sample_size = 10
sample = [0 for i in range(sample_size)]
current_index = 0
while True:
   data = ser.readline()
   data = str(data)[2:-5]
   try:
      sample[current_index] = int(data)
   except:
      sample[current_index] = 0
   current_index = current_index + 1 if current_index + 1 < sample_size else 0
   sma = int(sum(sample)/sample_size)
   print(data, sma)