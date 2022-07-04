# Toggle character

def CharToggle(c):
    if c >= 'A' and c <= 'Z':
       return chr(ord(c)+32)

    if c >= 'a' and c <= 'z':
        return chr(ord(c) - 32)

ch = input("Enter Character : ")
cRet = CharToggle(ch)
print("Toggle Character is : ",cRet)
        
    