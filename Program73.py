# count vowel 

def Count(str):
    iCnt = 0
    for i  in str:
        if i == 'a' or i == 'i' or i == 'o'or i == 'u' or i == 'e' or i == 'A' or i == 'I' or i == 'O'or i == 'U' or i == 'E':
           iCnt+=1
    return iCnt       

ch = input("Enter String : ")
iRet = Count(ch)
print("Count Vowel are : ",iRet)    