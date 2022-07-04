# Find maximum element in array

def Maximum(brr):
    iMax = brr[0]
    
    for i in brr:
        if i > iMax:
           iMax = i
    return iMax

arr = []

iValue = int(input("Enter Number of Elements : "))

for i in range(iValue):
    arr.append(int(input("Enter Number : "))) 

iRet = Maximum(arr)
print("Maximum Element  in array : ",iRet)    