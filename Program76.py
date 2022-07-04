# check pallindrome

def CheckPallindrome(str):
    
    srr = ''   
    for i in reversed(str):
        srr = srr + i
            
         
    if srr == str:
       return True
    else:
       return False
       
ch = input("Enter String : ").lower()
bRet = CheckPallindrome(ch)
if bRet == True:
   print("It is Pallindrome")
else:
   print("It is not Pallindrome")   