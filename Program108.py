# count vowel in given file
import os

file = input("Enter File name : ")

if os.path.exists(file):
   f = open(file,'r')
   f1 = f.read()
   iCnt = 0
   for i in f1:
       if (i == 'a')or(i == 'e')or(i == 'i')or(i == 'o')or(i == 'u'):
          iCnt+=1
   print("Number Vowel in given file data is : ",iCnt)

else:
    print("File not Exits")
    
          