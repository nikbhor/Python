# write data

import os

file = input("Enter Filename : ")

if os.path.isfile(file):
   f = open(file,'w')
   f.write("HEllo Data Write Successfully")
   print("Data Written Successfully in file")
else:
    print("File Not Exits")   
    