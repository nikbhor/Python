# Accept number and position of bit check its on or off

def CheckBit(iNo,iPos):
    iMask = 0x00000001
    iResult = 0
    if ((iPos < 1) or (iPos > 32)):
       return False
    
    iMask = iMask << (iPos - 1)
    iResult = iNo & iMask
    if iResult == iMask:
       return True
    else:
       return False

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iValue2 = int(input("Enter position : "))
   bRet = CheckBit(iValue,iValue2)
   if bRet == True:
      print("Bit is on")
   else:
      print("Bit is off")
      