# Swap bytes


def SwapBytes(iNo):
    return (iNo & 0x00FFFF00) | (iNo << 24) | (iNo >> 24)

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iRet = SwapBytes(iValue)
   print("Updated Number is : ",iRet)
   
    
