# Count number is greater than 10

def Count(brr):
    iCnt = 0
    
    for i in brr:
        if i > 10:
           iCnt += 1
    return iCnt
    
arr = []

iValue = int(input("Enter Number of elements : "))

for i in range(iValue):
    arr.append(int(input("Enter Element : ")))

iRet = Count(arr)
print("Count of Number is Greater than 10 : ",iRet)
       
    