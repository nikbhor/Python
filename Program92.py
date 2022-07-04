# importing module

from ArrayX import *

class Addition(ArrayX):
      def __init__(self,iNo):
          super().__init__(iNo)
      def Summation(self):
          iSum = 0
          for i in self.arr:
              iSum += i
          return iSum

iValue = int(input("Enter Size of element : "))
obj = Addition(iValue)          
obj.Accept()
obj.Display()
iRet = obj.Summation()
print("Addition of Array Element is : ",iRet)