# Check given number is perfect number or not

def CheckPerfect(iNo):
    if iNo < 0:
       iNo = - iNo
    iNumber = SumFactor(iNo)
    if iNumber == iNo:
       return True
    else:
       return False    
 
def SumFactor(iNo1):
    iSum = 0
    for i in range(1,((iNo1 // 2)+1)):
        if ((iNo1 % i) == 0):
        
            iSum += i
    
    return iSum

iValue = int(input("Enter Number : "))
iRet = CheckPerfect(iValue)

if iRet == True:
   print(" Is PerFect Number")   
else:
   print("Is not PerFect Number")
   
    
    
    
    