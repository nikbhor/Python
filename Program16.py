# summation of even digit of given number

def SumEvenDigit(iNo):
    if iNo == 0:
       return 0
       
    if iNo < 0:
       iNo = - iNo
    iSum = 0
    iDigit = 0

    while iNo != 0:
          iDigit = iNo % 10
          if ((iDigit % 2) == 0):
             iSum += iDigit
          iNo //= 10
    return iSum

iValue = int(input("Enter Number : "))
iRet = SumEvenDigit(iValue)
print("Sum of Even Digit is : ",iRet)
    