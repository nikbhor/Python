# seek data (that means read data from given position)

import os

file = input("Enter file name : ")
if os.path.isfile(file):
   f = open(file,'r')
   data = int(input("Enter Position Where you want to read : "))
   f.seek(data)
   print(f.read())
   f.close()
else:
   print("File not Exits")
   