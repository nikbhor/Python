# count even digit in array

def CountEven(brr):
    iCnt = 0
    for i in brr:
        if i % 2 == 0:
           iCnt+=1
    return iCnt       

arr = []
iValue = int(input("Enter Number of elements : ")) 

for i in range(iValue):
    arr.append(int(input("Enter Element : ")))

iRet = CountEven(arr)
print("Count of Even Number of Array : ",iRet)    
    