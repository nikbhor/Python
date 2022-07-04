# using static method 

class Addition:
      def AdditionNum(iNo,iNo2):
          return iNo + iNo2

iValue1 = eval(input("Enter First Number : "))
iValue2 = eval(input("Enter Second Number : "))

print(Addition.AdditionNum(iValue1,iValue2))          