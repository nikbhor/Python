# calculate power of given number 

def Power(iNo1, iNo2):
    iMult = 1
    if iNo1 < 0: 
       iNo1 = -iNo1
    if iNo2 < 0: 
       iNo2 = - iNo2
    
    for i in range(1,iNo2+1):
        iMult *= iNo1
    return iMult 

iValue1 = int(input("Enter First Number : "))
iValue2 = int(input("Enter Second Number : "))

iRet = Power(iValue1,iValue2)
print("Result is : ",iRet) 
   
        