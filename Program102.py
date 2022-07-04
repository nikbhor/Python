# append data on file

import os

file = input("Enter File name : ")

if os.path.isfile(file):
   f  = open(file,'a')
   data = input("Enter data on file : ")
   f.write(data)
   print("Data Appended successfully on file")
   f.close()
else:
   print("File not Exits Creating new file of given name.....") 
   f  = open(file,'a')
   data = input("Enter data on file : ")
   f.write(data)
   print("Data writted successfully on file")
   f.close()   
   