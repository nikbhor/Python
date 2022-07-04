class StringX:
      def Accept(self):
          self.str = input("Enter String : ")
      def Display(self):
          print("Your Entered String is : ",self.str)
class Reverce(StringX):
      def ReverceString(self):
          for i in reversed(self.str):
              print(i,end="")
      