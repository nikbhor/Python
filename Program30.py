# Input : 127894
# Output : 3

# Input : 561750
# Output : 4

def Count(iNo):
    iCnt = 0
    if iNo < 0:
       iNo = -iNo
       
    while iNo != 0:
          iDigit = iNo % 10
          if iDigit >= 5:
             iCnt+= 1
          iNo//=10
    return iCnt
    
iValue = int(input("Enter Number : "))
iRet = Count(iValue)
print("Digits greaterthan 5 are : ",iRet)
          