# check cursor position of file

import os
file = input("Enter File name : ")
if os.path.exists(file):
   f = open(file,'r')
   print(f.tell())
   f.seek(9)
   print(f.tell())
   f.read()
   print(f.tell())
   f.close()
else:
    print("File not Exits")   