# toggle range remove two variable iMask1 and iMask2

def ToggleOnRange(iNo,iStart,iEnd):
    iMask = (0xFFFFFFFF << (iStart - 1)) & (0xFFFFFFFF >> (32 - iEnd))
    return iNo ^ iMask
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   i = int(input("Enter Starting Position : "))
   j = int(input("Enter Ending Position : "))
   iRet = ToggleOnRange(iValue,i,j)
   print("Updated number is : ",iRet)
   
    