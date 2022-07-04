# last occurance of no. forword direction loop

def LastOccurance(brr,iNo):
    iIndex = -1
    iCnt = -1
    for i in brr:
        iCnt+=1
        if i == iNo:
           iIndex = iCnt
    return iIndex

arr = []

iValue = int(input("Enter Number of elements : "))
for i in range(iValue):
    arr.append(eval(input("Enter Element : ")))

iSearch = eval(input("Enter Number to Search : ")) 
iRet = LastOccurance(arr,iSearch)
if iRet == -1:
   print("Number is not there")
else:
   print("Last Occurance of Index is : ",iRet)   
        