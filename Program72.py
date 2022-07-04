# Calculate spaces of given string

def SpaceCount(str):
    i,iCnt = 0,0
    while i < len(str):
          if str[i] == ' ':
             iCnt+=1
          i+=1
    return iCnt
    
def CountSpace(str):
    Count = 0
    for i in str:
        if i == ' ':
           Count+=1
    return Count       
           

ch = input("Enter String : ")
iRet = SpaceCount(ch)
iRet2 = CountSpace(ch)
print("Spaces are : ",iRet)    
print("Spaces are : ",iRet2)    