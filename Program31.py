# Input :      6

# iCnt           1    2   3   4    5   6

# Output :    a    b   c   d   e   f


def DisplayAlphabet(iNo):
    if iNo < 0:
       iNo = -iNo

    for iCnt in range(iNo):
        print(chr(ord('a')+iCnt))

iValue = int(input("Enter Number : "))
DisplayAlphabet(iValue)