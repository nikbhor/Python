# Display Pattern 
# Row 3 
# Column 4

def Display(iRow,iCol):
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print("*",end="\t")
        print()

iValue1 = int(input("Enter Number Rows : "))
iValue2 = int(input("Enter Number Column : "))
Display(iValue1,iValue2)
        