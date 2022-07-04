#  Calculate average of array elements

def Average(brr):
    iSum = 0
    
    for i in brr:
        iSum += i
    iResult = iSum / len(brr)
    return iResult

arr = []
iValue=int(input("Enter number of Elements : ")) 

for i in range(iValue):
    arr.append(int(input("Enter Element : ")))
    
iRet = Average(arr)
print("Average is : {:.2f} ".format(iRet))    