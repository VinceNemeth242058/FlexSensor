import serial

def convertToDeg(resistance: int) -> int:
   return 180 - int((resistance - 0) * (180 - 0) / (255 - 0) + 0)

ser = serial.Serial("COM4", baudrate=9600, timeout=1)
sample_size = 10
sample = [0 for i in range(sample_size)]
current_index = 0
while True:
   data = ser.readline()
   data = str(data).replace("b'", "")[:-5].split()
   sample[current_index] = int(data[1]) if len(data) == 2 else 0
   current_index = current_index + 1 if current_index + 1 < sample_size else 0
   sma = int(sum(sample)/sample_size)
   print(current_index,sma,convertToDeg(sma),sample)