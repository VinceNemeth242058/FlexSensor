import pyautogui
import serial

import csv
import time
import os
from DegreeConverter import *
start = time.time()
ser = serial.Serial("COM4", baudrate=9600, timeout=1)
sample_size = 1
sample = [0 for i in range(sample_size)]
current_index = 0
dx = 0
prev_x = None

click = 0.3
csv_file_path = 'output_data.csv'
if os.path.exists(csv_file_path):
   os.remove(csv_file_path)
while True:
   data = ser.readline()
   data = str(data)[2:-5]
   try:
      sample[current_index] = int(data)
   except:
      sample[current_index] = 0
   vis = sample[current_index]
   
   current_index = current_index + 1 if current_index + 1 < sample_size else 0
   sma = int(sum(sample)/sample_size)
   calced = polynomial(sma)
   if prev_x == None:
      prev_x = calced
   else:
      dx = calced - prev_x
      prev_x = calced
   #if dx > click:
   #  print("\nClick!\n")
   #  pyautogui.click(pyautogui.position())
   with open(csv_file_path, mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([vis, calced, time.time() - start])
   print(f"Value: {vis} Calculated: {calced} ")
# 500 - 0.3 990 - 1.0
# 650 - 0.5 850 - 0.8