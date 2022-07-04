# Addition


class Addition:
      def __init__(self,iNo1,iNo2):
          self.iNo1 = iNo1
          self.iNo2 = iNo2
      def AdditionNum(self):
          return self.iNo1 + self.iNo2

iValue1 = eval(input("Enter first Number : "))
iValue2 = eval(input("Enter Second Number : "))
          
a = Addition(iValue1,iValue2)
b = a.AdditionNum()
print("Addition is : ",b)          
