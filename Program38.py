'''
    iRow = 6

    iCol = 6
 
    $   #   #  #
    *   $   #  #
    *   *   $   #
    *   *   *   $
 
'''

def Display(iRow,iCol):
    if iRow != iCol:
       return
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if i==j:
               print("$",end="\t")
            elif i >=j:
               print("*",end="\t")
            else:
               print("#",end="\t")
        print()

iValue1 = int(input("Enter Number of rows : "))        
iValue2 = int(input("Enter Number of Column : "))
Display(iValue1,iValue2)        
