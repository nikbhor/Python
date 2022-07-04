# input 4 
# Output 4 3 2 1

def DisplayRev(iNo):
    
    if iNo < 0:
       iNo = -iNo
    
    for i in range(iNo,0,-1):
        print(i,end="  ")

iValue = int(input("Enter Number : "))
DisplayRev(iValue)        