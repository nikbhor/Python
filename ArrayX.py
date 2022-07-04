class ArrayX:
      def __init__(self,iSize):
          self.iSize = iSize
          self.arr = []
      def Accept(self):
          for i in range(self.iSize):
              self.arr.append(int(input("Enter Number : ")))
      def Display(self):
          print("Element of Array : ")
          for i in self.arr:
              print(i,end=" ")
          print()    