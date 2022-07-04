# using flag check num is there in list/ array or not



def CheckNumber(brr):
    bflag = False
    for i in brr:
        if i == 11: 
           bflag = True
    return bflag

arr = []
iValue = int(input("Enter Number of Element : "))

for i in range(iValue):    
    arr.append(int(input("Enter Number : ")))

iRet = CheckNumber(arr)
if iRet == True:
   print("Number is There")
else:
   print("Number is Not there")
   
    