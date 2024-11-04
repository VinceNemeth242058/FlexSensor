import serial

ser = serial.Serial("COM5", baudrate=9600, timeout=1)
sample_size = 10
sample = [0 for i in range(sample_size)]
current_index = 0
while True:
   data = ser.readline()
   data = data.strip().split()
   sample[current_index] = data
   current_index = current_index + 1 if current_index - 1 < sample_size else 0
   print(sample)