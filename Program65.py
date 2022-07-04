# check digits

def CheckDigit(iNo):
    if iNo >= 0 and iNo <= 9:
       return True
    else:
       return False
       
       
ch =eval(input("Enter Digit from '0' to '9' : "))
bRet = CheckDigit(ch) 

if bRet == True:
   print("It is Digit")
else:
   print("It is Not Digit")
   