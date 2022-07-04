# Factorial 

def Factorial(iNo):
    iFact = 1
    
    if iNo < 0:        # Updator
       iNo = -iNo
       
    for i in range(1,iNo+1):
        iFact *= i
        
    return iFact

iValue = int(input("Enter Number : "))
iRet = Factorial(iValue)
print("Factorial is : ",iRet)    