# Display Digit of given number


def DisplayDigit(iNo):
    if iNo < 0:       # Updator
       iNo = -iNo
       
    iDigit = 0
    while iNo != 0:
          iDigit = iNo % 10
          print(iDigit)
          iNo = iNo // 10
          
       
          
iValue = int(input("Enter Number : "))
DisplayDigit(iValue)          