# Summation of array element

class ArrayX:
     def __init__(self,iSize):
         self.iSize = iSize
         self.arr = []
     def Accept(self):
         for i  in range(self.iSize):
             self.arr.append(eval(input("Enter Number : ")))

class Display(ArrayX):
      def __init__(self,iNo):
          super().__init__(iNo)
      def Display(self):
          print("Element of Array is : ")
          for i in self.arr:
              print(i,end=" ")

iValue = int(input("Enter Size of Array : "))
d = Display(iValue)
d.Accept()
d.Display()              
                              