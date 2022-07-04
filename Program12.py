# Sum of DIgit

def SumDigit(iNo):
    if iNo < 0:
       iNo = - iNo
    iDigit = 0
    iSum = 0
    
    while iNo != 0:
          iDigit = iNo % 10
          iSum += iDigit
          iNo = iNo // 10
    return iSum

iValue = int(input("Enter Number : "))
iRet = SumDigit(iValue)
print("Sum of Digit is : ",iRet)
    