# Toggle bit

def ToggleBit(iNo,iPos):
    iMask = 0x00000001
    iResult = 0
    iMask = iMask << (iPos - 1)
    iResult = iNo ^ iMask
    return iResult

if __name__ == "__main__":
   iValue = int(input("Enter Number : "))
   iValue2 = int(input("Enter Position of bit : "))
   iRet = ToggleBit(iValue,iValue2)
   print("Updated Number is : ",iRet)
   