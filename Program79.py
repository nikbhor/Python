# Display Binary


def DisplayBinary(iNo):
    if iNo >= 1:
          DisplayBinary(iNo // 2)
          print(iNo % 2,end="")

if __name__ == "__main__":
   iValue = int(input("Enter Number : "))
   DisplayBinary(iValue)          

print()
print("Without Recursion \n")   
   
# Without recursion

def DisplayBin(iNo):
    a = []
    while iNo != 0:
          iDigit = iNo % 2
          a.append(iDigit)
          iNo //= 2
    a.reverse()
    
    for i in a:
        print(i,end="")
    
if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   DisplayBin(iValue)   
    