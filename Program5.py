# Print Number with handling all Condition

def Display(iNo):
    if iNo == 0:
       print("Your Entered Number is Zero")
       return
    elif iNo < 0:
         iNo = -iNo
    
    for i in range(1,iNo+1):
        print(i)

iValue = int(input("Enter Number : "))
Display(iValue)        