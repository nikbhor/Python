# input 5 
# Output * # * # *

def Display(iNo):
    if iNo < 0:
       iNo = -iNo
    for i in range(1,iNo+1):
        if ((i % 2) == 0):
            print("#",end=" ")
        else:
           print("*",end=" ")   


iValue = int(input("Enter Number : "))
Display(iValue)           