# find factors of number

def DisplayFactor(iNo):
   
   if iNo < 0:
      iNo = - iNo
      
   for i in range(1,(iNo//2+1)):
        if ((iNo % i) == 0):
           print(i)

iValue = int(input("Enter Number : "))
DisplayFactor(iValue)    