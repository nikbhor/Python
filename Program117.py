# count number of bits are on using different condition

def CountBit(iNo):
    iMask = 0x00000001
    iResult = 0
    iCnt = 0
    for i in range(1,32):
        iResult = iNo & iMask
        if iResult == iMask:
           iCnt += 1
        iMask = iMask << 1 
    return iCnt

if __name__=="__main__":
   iValue = int(input("Enter File Name : "))
   iRet = CountBit(iValue)
   print("Total Number of on bit are : ",iRet)
   