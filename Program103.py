# read how many character you want

import os

file = input("Enter file name : ")

if os.path.isfile(file):
   f = open(file,'r')
   data = int(input("Enter how many character you want to read : "))
   print(f.read(data))
   f.close()
else:
  print("File is not exits")
  