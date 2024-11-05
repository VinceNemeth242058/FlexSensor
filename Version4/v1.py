import serial
from DegreeConverter import custom_scaling
import pyautogui



ser = serial.Serial("COM4", baudrate=9600, timeout=1)
sample_size = 1
sample = [0 for i in range(sample_size)]
current_index = 0
dx = 0
prev_x = None

click = 0.3

while True:
   data = ser.readline()
   data = str(data)[2:-5]
   try:
      sample[current_index] = int(data)
   except:
      sample[current_index] = 0
   
   
   current_index = current_index + 1 if current_index + 1 < sample_size else 0
   sma = int(sum(sample)/sample_size)
   calced = custom_scaling(sma)
   if prev_x == None:
      prev_x = calced
   else:
      dx = calced - prev_x
      prev_x = calced
   if dx > click:
      print("\nClick!\n")
      pyautogui.click(pyautogui.position())
   print("Value: ", calced)