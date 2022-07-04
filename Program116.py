# count number of bits is ON

def CountBit(iNo):
    iMask = 0x00000001
    iResult = 0
    iCnt = 0
    for i in range(1,32):
        iResult = iMask & iNo
        if iResult != 0:
           iCnt+=1
        iMask = iMask << 1
    return iCnt

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iRet = CountBit(iValue)
   print("Number of on bits are : ",iRet)   
        