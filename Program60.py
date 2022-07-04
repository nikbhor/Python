# Calculate length of string

def StrLen(str):
    
    i = 0
    while i < len(str):
          
          i += 1

    return i
    

ch = input("Enter String : ") 
iRet = StrLen(ch)
print("Length of string is : ",iRet)   
       

# using for loop

ch1 = input("Enter String Second String : ")
iCnt = 0
for i  in ch1:
    iCnt+=1
print("Length of String is : ",iCnt)    