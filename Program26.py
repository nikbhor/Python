# input 5 
# output 2 4 6 8 10 

def Display(iNo):
    if iNo < 0:
       iNo = - iNo
    for i in range(1,iNo+1):
        print(i*2,end="\t")

iValue = int(input("Enter Number : "))
Display(iValue)        
 