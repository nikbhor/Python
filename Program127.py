# Singly linked list   206

class Node:
      def __init__(self,data=None):
          self.data = data
          self.next = None

class SinglyLinkedList:
      def __init__(self):
          self.Head = None
      def Display(self):
          itemp = self.Head
          while itemp is not None:
                print(itemp.data)
                itemp = itemp.next                

list1 = SinglyLinkedList()
list1.Head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# LInk first node to second node
list1.Head.next = e2
e2.next = e3
list1.Display()
         