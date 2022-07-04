# Convert capital to small 

def CapitalToSmall(c):
    if c >= 'A' and c <= 'Z':
       return chr(ord(c) + 32)

ch = input("Enter Character : ")
cRet = CapitalToSmall(ch)
print("Small Letter is : ",cRet)       
