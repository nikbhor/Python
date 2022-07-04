# open file

import os

file = input("Enter File name : ")
if os.path.exists(file):
   f = open(file,'r')
   print("File open Successfully")
   f.close()
else:
  print("File doesn't Exits ")
  