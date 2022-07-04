# Toggle range of bit

def ToggleOnRange(iNo, iStart, iEnd):
    iMask1 = 0XFFFFFFFF
    iMask2 = 0XFFFFFFFF
    iMask1 = iMask1 << (iStart - 1)
    iMask2 = iMask2 >> (32 - iEnd)
    
    iMask = iMask1 & iMask2
    
   # iResult = iMask | iNo 
    iResult = iMask ^ iNo
    
    return iResult

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   i = int(input("Enter Starting position : "))
   j = int(input("Enter Ending Position : "))
   iRet = ToggleOnRange(iValue,i,j)
   print("Updated Number is : ",iRet)  


"""
FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF   iMask1 = 0XFFFFFFFF
FFFF FFFF FFFF FFFF FFFF FFFF FFFF 0000   istart = 5

FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF   iMask2 = 0XFFFFFFFF
0000 0000 0000 0000 FFFF FFFF FFFF FFFF   iEnd = 16

FFFF FFFF FFFF FFFF FFFF FFFF FFFF 0000    iStart = 5 iMask1 = iMask1 << (iStart - 1)
0000 0000 0000 0000 FFFF FFFF FFFF FFFF    iEnd = 16  iMask2 = iMask2 >> (32 - iEnd)
_____________________________________________  &  (bitwise and)
0000 0000 0000 0000 FFFF FFFF FFFF 0000       = Ans iMask = iMask1 & iMask2

0000 0000 0000 0000 0000 0000 0000 0010  
0000 0000 0000 0000 1111 1111 1111 0000
_________________________________________    | (bitwiawe or)
0000 0000 0000 0000 1111 1111 1111 0010      iResult = iMask | iNo
  
"""


     
    