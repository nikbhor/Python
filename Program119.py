# Toggle nibble
#
 #   //  1111    0000    0000    0000    0000    0000    0000    1111
  #  //      F       0           0           0       0           0           0       F
  #  // 0xF000000F

def ToggleNibble(iNo):
    iMask = 0xF000000F
    iResult = iNo ^ iMask
    return iResult

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   iRet = ToggleNibble(iValue)
   print("Updated number is : ",iRet)
   