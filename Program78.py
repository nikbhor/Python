# Reverce string

def StrRev(str):
    str1 = ''
    for i in reversed(str):
        str1 += i
    return str1

ch = input("Enter String : ")
cRet = StrRev(ch)
print("Reverce String is : ",cRet)

    