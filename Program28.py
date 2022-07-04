# caluculate Average

def Average(iNo1,iNo2,iNo3):
   iSum = iNo1+iNo2+iNo3
   iAvg = iSum / 3
   return iAvg

iValue1 = int(input("Enter First Number : "))   
iValue2 = int(input("Enter Second Number : "))   
iValue3 = int(input("Enter Third Number : ")) 

iRet = Average(iValue1,iValue2,iValue3)

print("Average is : ",iRet)
  