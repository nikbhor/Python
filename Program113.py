# Count size of file

import os

file = input("Enter File name : ")
if os.path.isfile(file):
   f = open(file,"r")
   #f1 = os.path.getsize(file)           # first way to get size
   #print("Size of file is : ",f1)
   iCnt = 0
   for i in f.read():                # second way to get size
       iCnt+=1
   print("Size of file is : ",iCnt)
   f.close()
else:
  print("file not Exists")
  