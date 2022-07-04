# Check prime number 


class Prime:
      def PrimeNum(self,iNo):
          bflag = True
          for i in range(2,(iNo+1)//2):
              if iNo % i == 0:
                 bflag = False
                 break 

          return bflag

iValue = int(input("Enter Number  : "))
p = Prime()          
bRet = p.PrimeNum(iValue)
if bRet == True:
   print("It is prime number")
else:
   print("It is not prime number")
   