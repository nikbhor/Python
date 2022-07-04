# count how many digit in given file

import os

file = input("Enter file name : ")

if os.path.isfile(file):
   f = open(file,"r")
   iCnt = 0
   for i in f.read():
       if i >= '0' and i <= '9':
          iCnt+=1
   print("Total number of digit are : ",iCnt)
else:
   print("File not Exits")
   
    