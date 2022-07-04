# Check bit is on or not

def CheckBit(iNo):
    iMask = 0X00000008
    iResult = iNo & iMask
    if iResult == iMask:
       return True
    else:
       return False    
       
if __name__ == "__main__":
   iValue = int(input("Enter Number : "))
   bRet = CheckBit(iValue)
   if bRet == True:
      print("4th bit is on")
   else:
      print("4th bit is off")   