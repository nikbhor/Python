# Display Minimum value  

def Minimum(iNo1, iNo2):
    if iNo1 < iNo2:
       return iNo1
    else:
       return iNo2

iValue1 = int(input("Enter First Number : "))
iValue2 = int(input("Enter Second Number : "))

iRet = Minimum(iValue1,iValue2)
print("Minimum Number is : ",iRet)
       