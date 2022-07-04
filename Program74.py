# Count character frequency

def CountFrequency(str,ch):
    i,iCnt = 0,0
    
    while i < len(str):
          if str[i] == ch:
             iCnt+=1
          i+=1
    return iCnt
    
ch = input("Enter String : ") 
cfreq = input("Enter Character : ")
iRet = CountFrequency(ch,cfreq)
print("Frequency of letter is : ",iRet)         