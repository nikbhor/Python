# Count Digit of Given number with small memory utilzation

def CountDigit(iNo):
    if iNo == 0:
       return 1
    if iNo < 0:
       iNo = - iNo
    iCnt = 0
    while iNo != 0: 
          iCnt += 1
          iNo //= 10
    return iCnt      

iValue = int(input("Enter Number : "))
iRet = CountDigit(iValue)
print("Count of Digit is : ",iRet)          
