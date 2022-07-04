# Display String


class StringX:
      def __init__(self):
          self.str=""
      def  Accept(self):
           self.str = input("Enter String : ")
      def Display(self):
          print("Your Entered String is : ",self.str)
          

sobj = StringX()
sobj.Accept()
sobj.Display()
          
                 
      