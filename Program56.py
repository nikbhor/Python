# last occurance of number in array


def LastOccurance(brr,iNo):
    iCnt = len(brr)  
    for i in range(len(brr)-1,-1,-1): # for i reversed(brr):
        iCnt -= 1
        if brr[i] == iNo:
           return iCnt
          
    return -1

arr = []

iValue = int(input("Enter Number of elements : "))
for i in range(iValue):  
    arr.append(int(input("Enter Number : ")))

iSearch = int(input("Enter Number to Search : "))
iRet = LastOccurance(arr,iSearch)
if iRet == -1:
   print("There is no such element")
else:
  print("Last Occurance index is : ",iRet)
  