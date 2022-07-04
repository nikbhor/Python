# count small letter

import os 

file = input("Enter File name : ")
if os.path.isfile(file):
   f = open(file,"r")
   iCnt = 0
   for i in f.read():
       if i >= 'a' and i <= 'z':
          iCnt+=1
   print("The number small letter are : ",iCnt)       
else:
   print("File is not Exits")
   