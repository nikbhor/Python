# check firstoccurance of number in array/list

def FirstOccurance(brr,iNo):
    iCnt = -1
    iIndex = 0
    for i in brr:
        iCnt += 1
        if i == iNo:
           return iCnt
    return -1      
           
           

       
       

arr = []

iValue = int(input("Enter Number of elements : "))

for i in range(iValue):
    arr.append(int(input("Enter Number : ")))

iSearch = int(input("Enter Number to Search : "))

iRet = FirstOccurance(arr,iSearch)
if iRet == -1:
   print("There is no such number")
else:
   print("First Occurance index is : ",iRet)
   