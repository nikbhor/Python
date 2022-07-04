# check pallindrome
from StringX import *
class Pallindrome(StringX):
      def CheckPallindrome(self):
          str = self.str.lower()
          srr = ""
          
          for i in str:
              srr = i + srr
              
          if srr == str:
             return True
          else:
             return False
             
pobj = Pallindrome()
pobj.Accept()
pobj.Display()

iRet = pobj.CheckPallindrome()
if iRet == True:
   print("It is Pallindrome")
else:
   print("It is not Pallindrome")
   