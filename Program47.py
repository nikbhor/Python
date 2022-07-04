# Sum of Odd NUmber of array

def SumOdd(brr):
    iSum = 0
    
    for i in brr:
        if i % 2 != 0:
           iSum += i
    return iSum

arr = []

iValue = int(input("Enter Number of elements : "))

for i in range(iValue):
    arr.append(int(input("Enter Number : ")))

iRet = SumOdd(arr)
print("Summation of Odd Number is : ",iRet)
    