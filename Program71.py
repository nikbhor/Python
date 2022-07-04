# Count capital and small Character in the given string

def Count(str):
    i,iCnt = 0,0
    CCount,SCount = 0,0
    
    while i < len(str):
          if str[i] >= 'A' and str[i] <= 'Z':
             CCount+=1
          if str[i] >= 'a' and str[i] <= 'z':
             SCount+=1
          i+=1
    #return CCount,SCount
    print("Capital Letter is : ",CCount)
    print("Small Letter is : ",SCount)
    
ch = input("Enter String : ")
iRet = Count(ch)
#print("Count of Capital and Small Letter is : ",iRet)    # output as form of tuple