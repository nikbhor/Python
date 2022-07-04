# Count bit without extra result variable

def CountBit(iNo):
    iMask = 0x00000001
    iCnt = 0
    for i in range(1,32):
        if (iNo & iMask) == iMask:
            iCnt+=1
        iMask = iMask << 1
    return iCnt
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iRet = CountBit(iValue)
   print("Number of On bit are : ",iRet)   