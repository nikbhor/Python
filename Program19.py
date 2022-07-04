# Check Palllindrome number of more functions

def CheckPallndrome(iNo):
    if iNo < 0:
       iNo = -iNo
    iNumber = 0
    iNumber = Reverse(iNo)
    if iNumber == iNo:
       return True
    else:
      return False

def Reverse(iNo):
       
    iDigit = 0
    iRev = 0
    
    while iNo != 0:
          iDigit = iNo % 10
          iRev = (iRev * 10) + iDigit
          iNo //= 10
    return iRev

iValue = int(input("Enter Number : "))
iRet = CheckPallndrome(iValue)

if iRet == True:
   print("Number is Palllindrome")
else:
   print("Number is Not Palllindrome")
   
       