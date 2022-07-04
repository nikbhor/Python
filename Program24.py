# input 5 
# output 1 * 2 * 3 * 4 * 5 *

def Display(iNo):
    if iNo < 0:
       iNo = -iNo
       
    for i in range(1,iNo+1):
        print(i," *",end="\t")

iValue = int(input("Enter Number : "))
Display(iValue)        