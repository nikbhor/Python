
def Display(iRow,iCol):
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print(i,end="\t")
        print()

iValue1 = int(input("Enter Number of Rows : "))
iValue2 = int(input("Enter Number of Column : "))
Display(iValue1,iValue2)        