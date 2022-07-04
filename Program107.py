# write data on file

import os 

file = input('Enter file name : ')
if os.path.isfile(file):
   f = open(file,'w+')
   f.write("*"*90)
   f.seek(0)
   print(f.read())
   f.close()
else:
   print("File not Exits Creating new file for your provided name....")
   f = open(file,'w+')
   f.write("*"*90)
   f.seek(0)
   print(f.read())
   f.close()
   
      