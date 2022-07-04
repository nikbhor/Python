# Check small letter

def CheckSmall(ch):
    if ch >= 'a' and ch <= 'z':
       return True
    else:
       return False

ch = input("Enter Character : ")
bRet = CheckSmall(ch) 

if bRet == True:
   print("It is Small")
else:
   print("It is not small")
   