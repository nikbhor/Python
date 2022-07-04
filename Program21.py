# Display Table
# input 5
# Output 5 10 15 20 25 30 35 40 45 50

def DisplayTable(iNo):
    if iNo == 0:
       return
       
    if iNo < 0:
       iNo = -iNo
       
    for i in range(1,10+1):
        print(iNo*i)

iValue = int(input("Enter Number : "))
DisplayTable(iValue)        