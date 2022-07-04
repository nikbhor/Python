# Count of Digit of given number

def CountDigit(iNo):
    
    if iNo < 0:  # Updator
       iNo = -iNo
    iDigit = 0
    iCnt = 0
    
    if iNo == 0:  # Input Updator
       return 1
       
    while iNo != 0:
          iDigit = iNo%10
          iCnt+=1
          iNo = iNo // 10
    return iCnt      
          
iValue = int(input("Enter Number : "))
iRet = CountDigit(iValue)
print("Count of Digit is : ",iRet)
          
