# Check Even number

def CheckEven(iNo):
    if ((iNo % 2) == 0):
       return True
    else:
      return False

iValue = int(input("Enter Number : "))
iRet = CheckEven(iValue) 
if iRet == True: 
   print("Is Even NUmber")
else: 
   print("Is not even number ")
   
          