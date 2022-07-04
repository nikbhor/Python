# Additon of element of array

def Addition(brr):
    iSum = 0
    for i in brr:
        iSum += i
    return iSum

arr = []
iValue = int(input("Enter Number of elements : "))

for i in range(iValue):
    arr.append(int(input("Enter Element : ")))
    
iRet = Addition(arr)

print("Addition of Array Element : ",iRet)
    