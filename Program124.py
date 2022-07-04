# Swapping bit

def SwapBit(iNo):
    iMask = 0x00FFFF00
    iTemp = iNo & iMask
    
    Byte1 = iNo << 24
    Byte4 = iNo >> 24
    
    iResult = iTemp | Byte1 | Byte4
    return iResult

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iRet = SwapBit(iValue)
   print("Updated number is : ",iRet)
   