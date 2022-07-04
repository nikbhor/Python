# using class 
import os 

class FILE:
      def __init__(self,name):
          self.f = open(name,'r')
      def __del__(self):
          self.f.close()
      def CountCapital(self):
          iCnt = 0
          for i in self.f.read():
              if i >= "A" and i <= "Z":
                 iCnt+= 1
          return iCnt 
          
      def CountSmall(self):
          self.f.seek(0)
          iCnt = 0
          for i in self.f.read():
              if i >= 'a' and i <= 'z':
                 iCnt+=1
          return iCnt
          
      def CountDigit(self):
          self.f.seek(0)
          iCnt = 0
          for i  in self.f.read():
              if i >= '0' and i <= '9': 
                 iCnt+=1
          return iCnt
          
      def CountSpace(self):
          self.f.seek(0)
          iCnt = 0
          for i in self.f.read():  
              if i == ' ':
                 iCnt+=1
          return iCnt
         
file = input("Enter File name : ")
if os.path.isfile(file):  
  f = FILE(file)
  iRet = f.CountCapital()
  print("Total Number of Capital letter are :  ",iRet)
    
  iRet = f.CountSmall()
  print("Total Number of Small letter are :  ",iRet)
    
  iRet = f.CountDigit()
  print("Total Number of Digit are :  ",iRet)
    
  iRet = f.CountSpace()
  print("Total Number of spaces are :  ",iRet)

else:
    print("File not Exists")  
  
               