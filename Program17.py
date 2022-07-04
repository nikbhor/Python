# Reverse Digit for given number

def ReverseNumber(iNo):
    
    if iNo < 0:
       iNo = - iNo
    
    Digit = 0
    iRev = 0
    while iNo != 0:
          iDigit = iNo % 10
          iRev = (iRev * 10) + iDigit
          iNo //= 10
    return iRev  
iValue = int(input("Enter Number : "))
iRet = ReverseNumber(iValue)
print("Reverse Number is : ",iRet)    