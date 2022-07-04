# print Sum of given number


def Summation(iNo):
    iSum = 0
    if iNo < 0:
       iNo = - iNo
    
    for i in range(1,iNo+1):
        iSum += i
    return iSum    
        
iValue = int(input("Enter Number : "))
iRet = Summation(iValue)
print("Addition is : ",iRet)        