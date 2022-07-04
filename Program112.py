# count number of spaces of given file

import os

file = input("Enter Name file : ")
if os.path.exists(file):
   f = open(file,"r")
   iCnt = 0
   for i in f.read():
       if i == ' ':
          iCnt+=1
   print("Total Number of Spaces is : ",iCnt) 
else:
   print("File Not Exists")
   