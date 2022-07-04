# Check Capital letter or not

def CheckCpital(ch):
    if ch >= 'A' and ch <= 'Z':
       return True
    else:
       return False

ch = input("Enter Character : ")
bRet = CheckCpital(ch)
if bRet == True:
   print("It is Capital")
else:
   print("It is not Capital")
   
   