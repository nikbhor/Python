# Check 11 is present in array or not

def CheckNumber(brr):
    for i in brr:
        if i == 11: 
           return True
    return False

arr = []
iValue = int(input("Enter Number of Element : "))

for i in range(iValue):    
    arr.append(int(input("Enter Number : ")))

iRet = CheckNumber(arr)
if iRet == True:
   print("Number is There")
else:
   print("Number is Not there")
   
    