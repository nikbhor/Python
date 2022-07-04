# Check amstrong number 

class Amstrong:
      @staticmethod
      def AmstrongNum(iNo):
          iSum = 0
          iPower = 1
          iTemp = iNo
          iDigCnt = 0
          while iTemp != 0:
              iDigCnt+=1
              iTemp//=10
          
          iTemp = iNo
    
          while iTemp != 0:
                iDigit = iTemp % 10
                for i in range(1,iDigCnt+1):
                    iPower*= iDigit 
                iSum += iPower
                iPower = 1
                iTemp //= 10
          if iNo == iSum:
             return True
          else:
             return False

a = Amstrong()
iNo = int(input("Enter number : "))
iRet = a.AmstrongNum(iNo)
if iRet == True:
   print("It is Amstrong Number")
else:
   print("It is Not Amstrong Number")   
              