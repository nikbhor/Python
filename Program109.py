# Count capital letter for given file

import os

file = input("Enter File name : ")
if os.path.isfile(file):
   f = open(file,'r')
   iCnt = 0
   for i in f.read():
       if i >= 'A' and i <= 'Z':
          iCnt+=1
   print("Total number of Capial Letter are : ",iCnt)
   f.close()   
else:
   print("File not Exists")   