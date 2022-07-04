# Print * 
# input 5 
# output * * * * * 

def Display(iNo):
    if iNo < 0:
       iNo = - iNo
       
    for i in range(1,iNo+1):
        print("*",end="\t")
 
iValue = int(input("Enter Number : "))
Display(iValue) 