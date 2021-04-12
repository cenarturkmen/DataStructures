from node import Node

class NodeD(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

dllist = DoublyLinkedList()
dllist.head = NodeD(1)
second = NodeD(2)
third = NodeD(3)
fourth = NodeD(4)

dllist.head.next = second
second.prev = dllist.head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

dllist.printList()

print(dllist.head.next.data)
print(dllist.head.next.next.prev.data)