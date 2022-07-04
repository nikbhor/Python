# Check pallindrome

def CheckPallindrome(str):
    flag = 0
    j = -1
   
    for i in str:
        if i != str[j]:
           flag = 1
        j=j-1    
         
    if flag == 1:
       return False
    else:
       return True
       
ch = input("Enter String : ")
bRet = CheckPallindrome(ch)
if bRet == True:
   print("It is Pallindrome")
else:
   print("It is not Pallindrome")   