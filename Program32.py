# Input 5
# Output A B C D E F

def DisplayAlphabet(iNo):
    for i in range(iNo):
        print(chr(ord('A')+i),end="  ")

iValue = int(input("Enter Number : "))
DisplayAlphabet(iValue)        