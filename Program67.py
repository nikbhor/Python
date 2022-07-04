# Convert Small to Capital 

def SmallToCapital(c):
    if c >= 'a' and c <= 'z':
       return chr(ord(c)-32)
       
ch = input("Enter Character : ")
cRet = SmallToCapital(ch)
print("Capital Letter is : ",cRet)
       