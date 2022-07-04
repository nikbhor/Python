# print Number in reverce order

def Display(iNo):
    if iNo == 0:
       print("Entered Number is Zero:")
    elif iNo < 0:
         iNo = -iNo
         
    for i in range(iNo,0,-1):
        print(i)
        
        
iValue = int(input("Enter Number : "))
Display(iValue)        