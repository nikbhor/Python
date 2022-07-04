# Check given number is pallindrome or not

def CheckPallindrome(iNo):
    if iNo < 0:
       iNo = - iNo
    iDigit = 0
    iRev = 0
    
    iTemp = iNo
    
    while iNo != 0:
          iDigit = iNo % 10
          iRev = (iRev * 10) + iDigit 
          iNo //= 10
    
    if iTemp == iRev:
       return True
    else:
       return False

iValue = int(input("Enter Number : "))
iRet = CheckPallindrome(iValue)

if iRet == True:
   print("Number is Pallindrome")
else:
   print("Number is Not Pallindrome")   