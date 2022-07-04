# read data from file

import os

file = input("Enter File name : ")

if os.path.isfile(file):
   f = open(file,"r")
   iRet = f.read()
   print("Data Read Successfully from the file")
   print("Data from file is : \n",iRet)
else:
   print("File Does not exits")
   
   