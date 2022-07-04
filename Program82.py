# check 7th and 12th bit is on or off

def CheckBit(iNo):
    iMask = 0X00000840
    iResult = iNo & iMask
    if iResult == iMask:
       return True
    else:
       return False
       
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   bRet = CheckBit(iValue)
   if bRet == True:
      print("7th and 12th bit is on")
   else:
      print("7th and 12th bit is off")
      