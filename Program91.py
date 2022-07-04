# Summation of array element

class ArrayX:
      def __init__(self,iSize):
          self.iSize = iSize
          self.arr = []
      def Accept(self):
          for i in range(self.iSize):
              self.arr.append(int(input("Enter Number : ")))
      def Display(self):
          print("Element of Array : ")
          for i in self.arr:
              print(i,end=" ")
              
class Addition(ArrayX):
      def __init__(self,iNo):
          super().__init__(iNo)
      def Sum(self):
          iSum = 0
          for i in self.arr:
              iSum += i
          return iSum

iValue = int(input("Enter Size of Array : "))
obj = Addition(iValue)          
obj.Accept()
obj.Display()
iRet = obj.Sum()
print()
print("Addition of Array Element is : ",iRet)
                