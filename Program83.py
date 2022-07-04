#check first four bit is on

def CheckBit(iNo):
    iMask = 0x0000000F
    iResult = iNo & iMask
    if iResult == iMask:
       return True
    else:
       return False
       
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   bRet = CheckBit(iValue)
   if bRet == True:
      print("First four bit is on") 
   else:
      print("First four bit is off")
      