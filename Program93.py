# print average 

from ArrayX import *

class Average(ArrayX):
      def __init__(self,iNo):
          super().__init__(iNo)
      def CalAverage(self):
          iSum = 0
          for i in self.arr:
              iSum += i  
          return iSum / len(self.arr);



iValue = int(input("Enter size of array : "))
a = Average(iValue)
a.Accept()
#a.Display()
iRet = a.CalAverage()
print("Average is : {:2f} ".format(iRet))          
                        