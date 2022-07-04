# count vowel in given string

class StringX:
      def Accept(self):
          self.str = input("Enter String : ")
      def Display(self):
          print(self.str)

class Vowel(StringX): 
      def CountVowel(self):
          iCnt = 0
          for i in self.str:
              if (i == 'a') or ( i == 'i') or (i == 'o') or (i == 'u') or (i == 'e')or (i == 'A')or(i=="I")or(i=="O")or(i=="U")or(i == "E"):
                  iCnt +=1
          return iCnt       
                
vobj = Vowel()
vobj.Accept()
vobj.Display() 
iret = vobj.CountVowel()
print("Number of Vowel present in the string : ",iret)         