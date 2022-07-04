# Get number from user to search in array

def CheckNumber(brr,iNo):
    bflag = False
    
    for i in brr:
        if i == iNo:
           bflag = True
    return bflag       
    

arr = []    
iValue = int(input("Enter Number of elements : "))

for i in range(iValue): 
    arr.append(int(input("Enter Number : ")))

iSearch = int(input("Enter Number to Search : "))
iRet = CheckNumber(arr,iSearch)
if iRet == True: 
   print("Number is there")
else:
   print("Number is Not there")
   