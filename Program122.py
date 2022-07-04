# ToggleOnRange without using extra variable

def ToggleOnRange(iNo,iStart,iEnd):
    return (iNo ^ ((0xFFFFFFFF << (iStart -1)) & (0xFFFFFFFF >> (32 - iEnd))))
    
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   i = int(input("Enter Starting Position : "))
   j = int(input("Enter Ending Position : "))
   iRet = ToggleOnRange(iValue,i,j)
   print("Updated Number are : ",iRet)
   