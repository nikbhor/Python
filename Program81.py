# Check 21st bit is on or off

def CheckBit(iNo):
    iMask = 0X00100000
    iResult = iNo & iMask
    if iResult == iMask:
       return True
    else:
       return False

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   bRet = CheckBit(iValue)
   if bRet == True:
      print("21st Bit is on")
   else:
      print("21st Bit is off")
      
    