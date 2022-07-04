# copy data from  to another file

import os

file = input("Enter file name : ")

if os.path.isfile(file):
   f =open(file,'r')
   newfile = input("Enter the file name You want to copy that data : ")
   f1 = open(newfile,'w')
   f1.write(f.read())
   print("Data copy successfully on new file")
   f.close()
   f1.close()
else:
   print("File not Exits")
   
   