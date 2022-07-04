# Find minimium number of array

def Minimum(brr):
    iMin = brr[0]
    
    for i in brr:
        if i < iMin:
           iMin = i
    return iMin

arr = []

iValue = int(input("Enter Number : "))

for i in range(iValue):
    arr.append(int(input("Enter Numbr : ")))

iRet = Minimum(arr)
print("Minimum Number in Array is : ",iRet)
    