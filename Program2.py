# Basic Addition Function


def Addition(iNo1, iNo2):
    iAns = iNo1 + iNo2
    return iAns
    

iValue1 = int(input("Enter First Number : "))    
iValue2 = int(input("Enter Second Number : "))    
iRet = Addition(iValue1,iValue2)
print("Addition is : ",iRet)
   