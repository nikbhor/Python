# count Number is Greater than 10 and less than 20

def CountRange(brr):
    iCnt = 0
    
    for i in brr:
        if i > 10 and i < 20:
           iCnt += 1
    
    return iCnt

arr = []
iValue = int(input("Enter Number of elements : ")) 

for i in range(iValue):
    arr.append(int(input("Enter Number : ")))

iRet = CountRange(arr)
print("Count of Element in Between 10 and 20 : ",iRet)    
   