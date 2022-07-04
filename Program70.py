# Calculate capital character of given string

def CapitalCount(str):
    i,iCnt = 0,0
    while i < len(str):
          if str[i] >= 'A' and str[i] <= 'Z':
             iCnt+=1
          i+=1
    return iCnt

ch = input("Enter String : ")
iRet = CapitalCount(ch)
print("Capital Letter is : ",iRet)
    