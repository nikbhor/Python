# Count Even digit of given number

def CountEvenDigit(iNo):
    if iNo == 0:
       return 1
    if iNo < 0:
       iNo = - iNo
       
    iCnt = 0
    while iNo != 0:
    
         iDigit = iNo % 10
         if ((iDigit % 2) == 0):
            iCnt += 1    
         iNo //= 10
    return iCnt

iValue = int(input("Enter Number : "))
iRet = CountEvenDigit(iValue)
print("Count of Even Digit is : ",iRet)
    