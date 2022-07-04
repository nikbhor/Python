# calculate small Character of string 

def CountSmall(str):
    i, iCnt  = 0,0
    while i < len(str):
          if str[i] >= 'a' and str[i] <= 'z':
             iCnt += 1
          i += 1   
    return iCnt 

ch = input("Enter String : ")
iRet = CountSmall(ch)
print("Small Character of string is : ",iRet)    