# Swapping character

def Swap(p,q):
    temp = p
    p = q
    q = temp
    return p,q

ch1 = input("Enter First Character : ")    
ch2 = input("Enter Second Character : ")    

print("Character Before swapping : ",ch1,ch2)
ch1,ch2 = Swap(ch1,ch2)    
print("Character After Swapping : ",ch1,ch2)
    